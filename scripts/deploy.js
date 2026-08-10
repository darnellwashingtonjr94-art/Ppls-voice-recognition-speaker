const hre = require("hardhat");

async function main() {
  console.log(">>> Initiating VoiceRegistry deployment...");

  // Fetch the compiled contract factory
  const VoiceRegistry = await hre.ethers.getContractFactory("VoiceRegistry");
  
  // Deploy the contract to the network
  const registry = await VoiceRegistry.deploy();
  await registry.waitForDeployment();

  console.log(`>>> VoiceRegistry successfully anchored to address: ${registry.target}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
