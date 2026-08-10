import time
import json
import logging

class DAWTelemetryMonitor:
    def __init__(self, daw_target="pro_tools", buffer_size=512, sample_rate=48000):
        self.daw_target = daw_target.lower()
        self.buffer_size = buffer_size
        self.sample_rate = sample_rate
        self.target_latency_ms = (buffer_size / sample_rate) * 1000.0
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("DAWTelemetry")

    def evaluate_block_performance(self, processing_time_ns: float) -> dict:
        """
        Evaluates processing time against strict DAW constraints:
        - Pro Tools HDX / Native: strict time-out constraints to avoid H/W buffer errors (-9128).
        - FL Studio: Mixer latency compensation tracking.
        """
        processing_ms = processing_time_ns / 1_000_000.0
        is_safe = processing_ms <= self.target_latency_ms
        headroom_ms = self.target_latency_ms - processing_ms

        metrics = {
            "daw": self.daw_target,
            "buffer_size": self.buffer_size,
            "sample_rate": self.sample_rate,
            "budget_ms": round(self.target_latency_ms, 3),
            "actual_ms": round(processing_ms, 3),
            "headroom_ms": round(headroom_ms, 3),
            "buffer_underrun_risk": not is_safe
        }

        if not is_safe:
            self.logger.warning(f"CRITICAL [{self.daw_target.upper()}] Buffer Underrun Risk! "
                                f"Took {processing_ms:.2f}ms of allowed {self.target_latency_ms:.2f}ms budget.")
        
        return metrics

if __name__ == "__main__":
    # Test Pro Tools native buffer profile (512 samples at 48kHz = ~10.66ms budget)
    pt_monitor = DAWTelemetryMonitor(daw_target="pro_tools", buffer_size=512, sample_rate=48000)
    print(json.dumps(pt_monitor.evaluate_block_performance(4500000), indent=2)) # 4.5ms processing time
    
    # Test FL Studio high-performance mixer profile (192 samples at 44.1kHz = ~4.35ms budget)
    fl_monitor = DAWTelemetryMonitor(daw_target="fl_studio", buffer_size=192, sample_rate=44100)
    print(json.dumps(fl_monitor.evaluate_block_performance(3200000), indent=2)) # 3.2ms processing time
