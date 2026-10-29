# Blinded Review: SP_ANON_147
**Composite Score:** 9.0 / 10.0 (Rigor: 3.1/3.5 | Claims: 2.3/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.9/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept (Minor Revision)
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This manuscript presents Datamonkey 3, a browser-native re-architecture of the Datamonkey molecular evolution platform that compiles the HyPhy statistical engine to WebAssembly (Wasm) via the Aioli runtime and executes analyses locally inside a dedicated browser Web Worker. The platform combines client-side FASTA/NEXUS validation and repair, interactive phylogenetic branch partitioning (`phylotree.js`), data-driven runtime estimation, IndexedDB local storage, an optional Socket.IO bridge to backend HPC clusters for alignments exceeding browser memory limits, and a Model Context Protocol (MCP) server for programmatic and AI-assisted workflows. The authors benchmark single-threaded native HyPhy (with ARM NEON SIMD) against headless Chromium Wasm across 6 curated representative datasets and a stratified corpus of 100 real-world alignments.

The engineering architecture is clean, genuinely solves the upload latency, queue contention, and data-sovereignty bottlenecks of centralized bioinformatics web servers, and is supported by a transparent performance benchmark that explicitly controls for survivor/timeout bias. Minor critiques concern the single-run cold-start benchmark design (which likely exaggerates Wasm overhead on fast methods like SLAC) and the distinction between single-core and multi-core native baselines on modern user hardware.

---

### 2. Methodological & Statistical Audit
* **Survivor-Bias-Controlled Wasm vs. Native Benchmarking:** In Table 2, the authors evaluate 100 real-world alignments stratified by `sequence × site` complexity and explicitly restrict both CLI and Wasm averages to the matched subset of datasets (75–87 per method) that completed within browser execution limits in both environments. This prevents differential timeout censoring on the largest alignments from artificially deflating Wasm mean runtimes.
* **Cold-Start JIT Overhead and Single-Run Variance in SLAC vs. Likelihood Methods:** As noted in the Table 2 caption, each method–dataset pair was executed once per environment without separate warm-up runs. Because SLAC is a fast counting-based method (mean CLI runtime 101.7s vs. 347–730s for likelihood methods), one-time Chromium Wasm module instantiation, virtual filesystem mounting, and V8 Liftoff-to-TurboFan JIT tier-up overhead represent a larger fraction of total wall-clock time, alongside integer/memory-access patterns that do not benefit from floating-point likelihood hot loops. Separating one-time Wasm initialization/JIT compilation latency from steady-state computation (or reporting median runtimes alongside means across 3–5 repeats) would clarify why SLAC exhibits a +405.9% mean slowdown compared to +67.1%–93.2% for aBSREL, BUSTED, FEL, and MEME.
* **Single-Core vs. Multi-Core Native Comparison Context:** Table 2 appropriately uses single-threaded native execution (with ARM NEON SIMD) as the like-for-like architectural baseline because the current Datamonkey 3 Wasm worker runs on a single thread. However, because native desktop HyPhy uses multi-core OpenMP parallelization across all available CPU cores (illustrated qualitatively in Figure 2), users comparing local CLI HyPhy on an 8–16 core workstation against browser execution will experience the combined effect of the ~1.8× Wasm instruction penalty and the $1\text{-thread vs. }N\text{-thread}$ scaling gap. Noting whether future Wasm builds will enable WebAssembly SIMD (`wasm-simd128`) and `SharedArrayBuffer`/pthread multi-threading would strengthen the technical discussion.

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Viability of Client-Side Browser Execution for Standard-Scale Molecular Evolution Analyses [Well Supported]:** The empirical complexity guidelines (`sequence × site` products $< 50,000$ completing in $< 30$ min for likelihood methods and $< 200,000$ for FEL/SLAC, with 100–400 MB RAM per 10,000 products) are directly grounded in the 100-alignment benchmark and provide practical operational boundaries for end users.
* **Zero-Server Data Sovereignty and Offline Capability [Well Supported]:** Local execution in a Web Worker with IndexedDB persistence ensures sensitive clinical or pre-publication pathogen sequences never leave the client device unless the user explicitly opts into backend HPC offloading.

---

### 4. Reproducibility & Data Completeness
* **Open-Source Availability:** The complete application (`[GITHUB_REPO_REDACTED]`, MIT license), live deployment (`v3.datamonkey.org`), and MCP endpoint (`mcp.datamonkey.org/mcp`) are publicly available.
* **Typographical Fixes Required:** In the section comparing performance on the 100 alignments, fix the garbled typesetting strings *"sequence bisite products"* and *"sequence itsite products"* to *"sequence $\times$ site products"*, and include a link or supplementary table listing the 100 benchmark alignments and their individual CLI/Wasm runtimes so the benchmark itself is fully reproducible.
