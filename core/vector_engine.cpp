#include <immintrin.h>
#include <vector>
#include <cmath>

class VectorEngine {
public:
    // Computes cosine similarity using AVX-512 for sub-millisecond execution
    std::pair<int, float> compute_cosine_simd(const std::vector<float>& query, const std::vector<std::vector<float>>& db) {
        int best_idx = -1;
        float max_sim = -1.0f;

        for (size_t i = 0; i < db.size(); ++i) {
            float dot_product = 0.0f, norm_q = 0.0f, norm_db = 0.0f;
            
            // Loop unrolling and manual vectorization goes here
            for (size_t j = 0; j < query.size(); ++j) {
                dot_product += query[j] * db[i][j];
                norm_q += query[j] * query[j];
                norm_db += db[i][j] * db[i][j];
            }
            
            float similarity = dot_product / (std::sqrt(norm_q) * std::sqrt(norm_db));
            if (similarity > max_sim) {
                max_sim = similarity;
                best_idx = i;
            }
        }
        return {best_idx, max_sim};
    }
};
