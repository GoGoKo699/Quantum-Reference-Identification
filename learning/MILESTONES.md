# Thirty milestones for Quantum Reference Identification

[Learning route](README.md) · [Scientific account](../science/README.md)

This is a project-defined understanding map for any reader. Its sole educational anchor is John Watrous, *The Theory of Quantum Information* (2018), using the author's [official pre-publication PDF](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf). Section references below follow that version. The anchor supplies the state, measurement, discrimination and invariant-measure framework; the linked project sources supply the specialized arguments and their research-level dependencies.

The allocation is **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The background combines the local objects into the complete delayed-query experiment. The narrative builds the quantum and classical proofs, then joins their resource and scope conditions into the scientific conclusion. More space goes to that narrative because the result depends on connecting several short arguments across an irreversible measurement boundary. This map does not replace the complete proofs or cover every neighboring topic.

## Background and preliminaries: M01–M12

### M01 — Physical states and descriptions

- **Central question:** What exactly is supplied to a quantum reference-identification algorithm?
- **Understanding target:** Distinguish a physical unknown state, its label, and a classical specification of its amplitudes. Explain why one does not automatically grant the other.
- **Dependencies and story role:** No earlier milestones; identify the individual input objects before combining them.
- **Conceptual connection:** Registers turn the phrase “quantum database” into a concrete collection of physical systems with a single-label output.
- **Source pointers:** Watrous §2.1.1–§2.1.2; [model: delayed membership query](../science/model.md#a-delayed-membership-query).

### M02 — Pure states, mixtures and ignorance

- **Central question:** How can each reference be pure while an averaged reference is mixed?
- **Understanding target:** Explain the density-operator description and separate randomness in preparation from a claim that an individual supplied specimen is physically maximally mixed.
- **Dependencies and story role:** M01; give each physical object a mathematical state before introducing copies.
- **Conceptual connection:** Bayesian averaging is the source of tractable hypothesis operators, not an extra depolarizing operation on the input.
- **Source pointers:** Watrous §2.1.2; [model: symmetric spaces](../science/model.md#symmetric-spaces); [Haar-averaged hypotheses](../science/quantum_identification.md#haar-averaging-gives-flat-projector-hypotheses).

### M03 — Copies and composite registers

- **Central question:** What information is present in several copies of one unknown state?
- **Understanding target:** Read a tensor-power state, distinguish it from independent draws of different states, and keep reference-copy and query-copy budgets separate.
- **Dependencies and story role:** M01–M02; combine specimens into a reference block and a query block.
- **Conceptual connection:** Supplied copies are a resource; writing a tensor power does not provide a cloning operation or a preparation oracle.
- **Source pointers:** Watrous §2.1.2; [model](../science/model.md#a-delayed-membership-query); [resource convention](../science/model.md#resource-convention).

### M04 — Reductions and averaging spectators

- **Central question:** How do the other reference blocks disappear from a one-label calculation?
- **Understanding target:** Explain partial trace and averaging over an independent spectator block, while preserving the correlations between a selected reference and its query.
- **Dependencies and story role:** M02–M03; connect local blocks to the complete library state.
- **Conceptual connection:** The same reduction principle later produces scalar projector traces and positive conditional classical-training posteriors.
- **Source pointers:** Watrous §2.1.3; [pair and triple overlaps](../science/quantum_identification.md#exact-pair-and-triple-overlaps); [collective-training posteriors](../science/classical_preprocessing.md#a-collective-training-measurement-still-has-positive-one-label-posteriors).

### M05 — A measurement that returns a label

- **Central question:** How is the probability of a correct identification defined?
- **Understanding target:** Explain positive measurement effects summing to the identity, the Born rule, and averaging over the uniform label and random library.
- **Dependencies and story role:** M01–M04; turn the physical experiment into a precise decision problem.
- **Conceptual connection:** Every permitted retained-quantum strategy has a joint POVM description, whereas a Bayesian guarantee need not hold for each fixed library.
- **Source pointers:** Watrous §2.3.1–§2.3.2 and §3.1.2; [model](../science/model.md#a-delayed-membership-query); [fixed and typical libraries](../science/quantum_identification.md#fixed-and-typical-libraries).

### M06 — Channels, records and measurement disturbance

- **Central question:** Why must a sequential decoder specify more than the probability that a test accepts?
- **Understanding target:** Distinguish an outcome probability from the corresponding change of state. Explain a measurement instrument and how a classical record can control a later operation.
- **Dependencies and story role:** M03–M05; add the temporal behavior of operations to the static measurement description.
- **Conceptual connection:** A valid rejection branch is needed for the scan; discarding every quantum training output creates the classical-preprocessing boundary.
- **Source pointers:** Watrous §2.2.1–§2.2.3 and §2.3.1–§2.3.2; [sequential decoder](../science/quantum_identification.md#sequential-symmetry-decoder); [clean reflection](../science/resources.md#a-clean-reflection-from-permutation-averaging).

### M07 — The symmetric subspace

- **Central question:** Which part of a many-register space contains identical pure-state copies?
- **Understanding target:** Explain permutation invariance, the symmetric projector and its dimension. Distinguish symmetry of vectors from a statement that every operator on several registers is symmetric.
- **Dependencies and story role:** M03 and M06; identify the geometric support on which the comparison test acts.
- **Conceptual connection:** Symmetry is both an information constraint and an observable that can be implemented without knowing the state amplitudes.
- **Source pointers:** Watrous §7.1.1; [symmetric spaces](../science/model.md#symmetric-spaces); [permutation-average projector](../science/resources.md#a-clean-reflection-from-permutation-averaging).

### M08 — Haar moments as invariant averages

- **Central question:** Why does averaging identical Haar copies give the normalized symmetric projector?
- **Understanding target:** Connect unitary invariance, support on the symmetric subspace, and normalization by its dimension. Explain the role of the input prior.
- **Dependencies and story role:** M02–M04 and M07; connect geometry to the actual random-library ensemble.
- **Conceptual connection:** The Haar moment identity converts an unknown-state classification problem into explicit finite-dimensional operators.
- **Source pointers:** Watrous §7.1.1 and §7.2.1–§7.2.2; [symmetric-space notation](../science/model.md#symmetric-spaces); [averaged hypotheses](../science/quantum_identification.md#haar-averaging-gives-flat-projector-hypotheses).

### M09 — Ensemble discrimination and a null comparison

- **Central question:** How can an operator inequality limit every possible decoder?
- **Understanding target:** Explain why a common positive upper bound on all hypothesis states yields a success bound after summing POVM effects. Keep a converse separate from a constructed measurement.
- **Dependencies and story role:** M05 and M08; prepare a global statement from local operator bounds.
- **Conceptual connection:** Comparing a correlated hypothesis to an independent null state is the short route to the finite-query capacity converse.
- **Source pointers:** Watrous §3.1.2; [finite-dimensional bounds](../science/quantum_identification.md#finite-dimensional-bounds); [averaged hypotheses](../science/quantum_identification.md#haar-averaging-gives-flat-projector-hypotheses).

### M10 — Spectra, support inverses and Gram matrices

- **Central question:** What information is gained by replacing overlapping subspaces with their Gram spectrum?
- **Understanding target:** Explain positive square roots, inverses restricted to support, and how a Gram matrix shares nonzero eigenvalues with a sum of projectors while retaining different zero multiplicities.
- **Dependencies and story role:** M05 and M07–M09; prepare the spectral language used for both achievability and error accumulation.
- **Conceptual connection:** A success construction uses an inverse square root; an all-decoder converse uses the deficit of a square-root trace.
- **Source pointers:** Watrous §1.1.3 and §3.1.2; [pretty-good measurement](../science/quantum_identification.md#pretty-good-measurement); [three-moment converse](../science/quantum_identification.md#error-converse-from-three-moments).

### M11 — Conditional likelihoods after training

- **Central question:** How does a classical training outcome change the distribution of the later query?
- **Understanding target:** Explain conditional probabilities and likelihoods relative to Haar measure. Distinguish a uniform prior label from the generally nonuniform conditional query marginal.
- **Dependencies and story role:** M04–M06 and M08; connect measurement outcomes with the later classical decision problem.
- **Conceptual connection:** Positive one-label posterior operators let a collective training measurement be analyzed without pretending its outcomes factor by reference.
- **Source pointers:** Watrous §1.2.2, §2.1.3 and §2.3.2; [collective-training posteriors](../science/classical_preprocessing.md#a-collective-training-measurement-still-has-positive-one-label-posteriors).

### M12 — The complete delayed-query experiment

- **Central question:** Which comparison isolates the value of retaining a quantum reference?
- **Understanding target:** Reconstruct the retained-quantum, classical-training and exactly revealed-query experiments, specifying when each input is available, what survives training, what is optimized, and which resources are charged.
- **Dependencies and story role:** M01–M11; integrate the background into the full problem rather than introduce another isolated definition.
- **Conceptual connection:** Chronology and resource matching determine which later inequalities express a quantum-memory advantage.
- **Source pointers:** Watrous §2.1–§2.3 and §3.1.2; [model](../science/model.md); [complete resource account](../science/resources.md#complete-input-and-memory-account); [interpretation](../science/interpretation.md).

## Narrative and innovation: M13–M30

### M13 — Correlation becomes a projector hypothesis

- **Central question:** What distinguishes the correct reference after averaging unknown state amplitudes?
- **Understanding target:** Derive the flat projector form of each hypothesis and explain why the query is jointly symmetric with precisely the selected reference block.
- **Dependencies and story role:** M07–M09 and M12; begin the contribution from its local correlated block.
- **Conceptual connection:** The rank ratio between a hypothesis support and the full input support defines the capacity parameter used throughout the finite-query result.
- **Source pointers:** Watrous §7.1.1 and §7.2.1; [Haar-averaged projector hypotheses](../science/quantum_identification.md#haar-averaging-gives-flat-projector-hypotheses).

### M14 — Pair and triple overlap identities

- **Central question:** How does independence control products of projectors that do not commute?
- **Understanding target:** Explain the spectator partial-trace step and obtain the second and third trace moments, keeping repeated and distinct label indices separate.
- **Dependencies and story role:** M04, M10 and M13; build the overlap data before applying either decoder or converse machinery.
- **Conceptual connection:** The third moment rules out an ambiguity pattern that pair overlaps alone could leave unresolved.
- **Source pointers:** Watrous §2.1.3 and §7.2.1; [exact overlaps](../science/quantum_identification.md#exact-pair-and-triple-overlaps); [error converse](../science/quantum_identification.md#error-converse-from-three-moments).

### M15 — The all-decoder capacity converse

- **Central question:** Why can no joint measurement overcome an insufficient hypothesis-support ratio?
- **Understanding target:** Apply the null-state operator comparison to every POVM and interpret the resulting success ceiling, including the random-guessing and no-reference limits.
- **Dependencies and story role:** M09, M12–M13; promote the local support calculation to a global impossibility statement.
- **Conceptual connection:** An unrestricted measurement converse is stronger than a failure analysis for a particular scan, while remaining Bayesian in the Haar library.
- **Source pointers:** Watrous §3.1.2; [finite-dimensional bounds](../science/quantum_identification.md#finite-dimensional-bounds); [averaged hypotheses](../science/quantum_identification.md#haar-averaging-gives-flat-projector-hypotheses); [model edge cases](../science/model.md#symmetric-spaces).

### M16 — An achievable information-theoretic frontier

- **Central question:** How can overlapping support projectors define a successful measurement?
- **Understanding target:** Explain the pretty-good measurement, its support inverse, and the Jensen and Cauchy–Schwarz steps giving its success lower bound.
- **Dependencies and story role:** M10 and M13–M15; pair the converse with a valid measurement at the same success order.
- **Conceptual connection:** Achievability of a probability frontier does not establish a fast implementation of the global inverse square root.
- **Source pointers:** Watrous §1.2.1 and §3.1.2; [pretty-good measurement](../science/quantum_identification.md#pretty-good-measurement).

### M17 — A scan that survives earlier rejections

- **Central question:** Why can one query block be used in a sequence of noncommuting tests?
- **Understanding target:** Explain the reject-earlier-labels/accept-correct-label path and the noncommutative union-bound guarantee. Distinguish it from unjustified independence of successive outcomes.
- **Dependencies and story role:** M06, M12–M14 and M16; replace the abstract measurement by a constructive sequential decoder.
- **Conceptual connection:** An inherited disturbance bound yields the same success order and an explicit small-error algorithm using the supplied specimens.
- **Source pointers:** Watrous §2.2–§2.3 and §3.1.2 for the instrument/discrimination framework; [sequential decoder](../science/quantum_identification.md#sequential-symmetry-decoder), which states and attributes the additional Gao bound.

### M18 — Why errors accumulate with many labels

- **Central question:** What prevents every false label from sharing one negligible ambiguous component?
- **Understanding target:** Follow the specialized trace bound, retain Gram zero eigenvalues, and connect the three exact moments to a quantitative error lower bound for every decoder.
- **Dependencies and story role:** M10 and M14–M17; strengthen a coarse success threshold into the all-accuracy error law.
- **Conceptual connection:** The new ensemble evaluation uses an inherited discrimination inequality; neither the inequality nor its generic spectral ingredients are claimed as new.
- **Source pointers:** Watrous §1.1.3 and §3.1.2 for matrix norms and discrimination; [three-moment error converse](../science/quantum_identification.md#error-converse-from-three-moments), including the additional Tyson dependency.

### M19 — Capacity, dimension and library quantifiers

- **Central question:** When can the finite-dimensional frontier be read as a query-copy scaling law?
- **Understanding target:** Combine the upper and lower bounds, retain the dimension condition when replacing capacity by a binomial coefficient, and distinguish Haar-average claims from deterministic or typical-library guarantees.
- **Dependencies and story role:** M12–M18; integrate the quantum bounds before turning to circuit realization and classical preprocessing.
- **Conceptual connection:** A fixed-reference query scale is a resource tradeoff; its sufficient separated-library conditions are not an all-library converse.
- **Source pointers:** Watrous §1.2.2 and §7.2.1–§7.2.2; [finite-query frontier](../science/interpretation.md#finite-query-frontier); [fixed and typical libraries](../science/quantum_identification.md#fixed-and-typical-libraries).

### M20 — From a symmetry average to a true instrument

- **Central question:** How is the required rejection channel obtained from permutation averaging?
- **Understanding target:** Explain the prepare–select–unprepare block, its clean reflection, and the flag measurement that produces the two Lüders branches while returning the ideal workspace.
- **Dependencies and story role:** M06–M07 and M17; implement the precise local operation assumed by the scan proof.
- **Conceptual connection:** An acceptance block equal to a projector is not by itself a proof of the correct Lüders rejection instrument; the reflection closes that implementation gap.
- **Source pointers:** Watrous §2.2.2–§2.2.3, §2.3.1 and §7.1.1; [clean-reflection construction](../science/resources.md#a-clean-reflection-from-permutation-averaging). The circuit construction is supplied locally rather than attributed to the anchor.

### M21 — Finite precision and complete costs

- **Central question:** What resources are needed for the constructive identification guarantee?
- **Understanding target:** Account for all supplied copies, stored data, active registers, comparisons and finite-gate precision. Explain why per-test approximation errors must shrink with scan length.
- **Dependencies and story role:** M12 and M17–M20; turn a mathematical instrument into a finite-resource algorithm statement.
- **Conceptual connection:** Channel-distance composition controls statistical error, while a polynomial circuit and a copy advantage do not establish a runtime advantage.
- **Source pointers:** Watrous §3.3.2–§3.3.3; [gate count and precision](../science/resources.md#gate-count-and-precision); [complete resource account](../science/resources.md#complete-input-and-memory-account), including the separately attributed synthesis dependency.

### M22 — Collective training without a factorization assumption

- **Central question:** How can all possible classical training records be bounded at once?
- **Understanding target:** Derive the positive effective operator for each label after an arbitrary collective reference measurement, and normalize its posterior likelihood correctly.
- **Dependencies and story role:** M04, M11–M12; begin the classical argument from the most general allowed local conditional object.
- **Conceptual connection:** Unlimited classical storage does not remove the information constraint expressed by a positive density operator on the symmetric reference space.
- **Source pointers:** Watrous §2.1.3 and §2.3.1–§2.3.2; [collective-training posterior proof](../science/classical_preprocessing.md#a-collective-training-measurement-still-has-positive-one-label-posteriors).

### M23 — A moment converse even for a perfect later query

- **Central question:** Why can later query information fail to repair the earlier measurement loss?
- **Understanding target:** Apply Haar moments to a posterior likelihood, bound its powers, and convert the maximum over labels into a finite-dimensional success ceiling valid for every collective training outcome.
- **Dependencies and story role:** M08–M11 and M22; promote the posterior constraint to an all-protocol classical converse.
- **Conceptual connection:** Giving away the exact later query strengthens the decoder, so the resulting ceiling also covers every finite query-copy budget under the same chronology.
- **Source pointers:** Watrous §1.2.1–§1.2.2 and §7.2.1; [finite-dimensional revealed-query converse](../science/classical_preprocessing.md#finite-dimensional-revealed-query-converse).

### M24 — A covariant classical strategy

- **Central question:** Can an actual classical training protocol approach that ceiling?
- **Understanding target:** Explain the independent covariant reference measurements and maximum-likelihood lookup, deriving their exact success in terms of the largest Haar overlap. Keep protocol performance separate from the finite-parameter optimum.
- **Dependencies and story role:** M05, M08, M11 and M22–M23; construct a matching candidate instead of relying on a converse alone.
- **Conceptual connection:** A continuous classical estimate is permitted by unlimited record storage; its copy cost is still the same supplied reference budget.
- **Source pointers:** Watrous §2.3 and §7.2.1–§7.2.2; [exact covariant strategy](../science/classical_preprocessing.md#a-classical-strategy-with-an-exact-finite-dimensional-success-formula).

### M25 — Optimizing the classical moment bound

- **Central question:** How does a finite integer-moment inequality produce the sharp logarithmic ceiling?
- **Understanding target:** Explain the moment-order choice proportional to the logarithm of the label count, the factorial estimate, and the cancellation that fixes the leading constant when the reference-copy count is fixed.
- **Dependencies and story role:** M23–M24; extract the global asymptotic upper bound without strengthening its quantifiers.
- **Conceptual connection:** A lower bound on the large symmetric dimension is sufficient; an unnecessary relative approximation would impose an unnecessarily strong dimension condition.
- **Source pointers:** Watrous §1.2.1–§1.2.2 for analytic and probabilistic tools; [asymptotic upper proof](../science/classical_preprocessing.md#upper-bound). The optimization and Stirling step are supplied in the project proof.

### M26 — Extreme overlaps close the asymptotic sandwich

- **Central question:** Why does the covariant strategy attain the same leading ceiling?
- **Understanding target:** Transform Haar overlaps into exponential variables, control the maximum and its fixed moments, and combine that estimate with the converse. State the fixed-reference and growing-dimension assumptions explicitly.
- **Dependencies and story role:** M24–M25; integrate the classical upper and lower arguments into the sharp saturation theorem.
- **Conceptual connection:** The theorem concerns a fixed scarce-reference budget; substituting a growing copy count into its asymptotic would change the claim.
- **Source pointers:** Watrous §1.2.2 and §7.2.1–§7.2.2; [attaining lower proof](../science/classical_preprocessing.md#attaining-lower-bound); [the sharp theorem](../science/classical_preprocessing.md#sharp-asymptotic-ceiling-for-a-fixed-reference-budget).

### M27 — The inherited finite-query obstruction

- **Central question:** How does a state-independent posterior component obstruct finite-query classification?
- **Understanding target:** Explain the positive measure-and-prepare decomposition and why its common component cannot identify a label. Distinguish this bound from the sharper ceiling that survives a perfectly revealed query.
- **Dependencies and story role:** M06, M08 and M22–M26; locate an important related mechanism within the completed classical account.
- **Conceptual connection:** A useful finite-query separation follows from established channel machinery; attribution prevents that inherited mechanism from absorbing the new claim.
- **Source pointers:** Watrous §2.2.2–§2.2.3 and §7.2.2 for the channel and averaging framework; [common-component account](../science/classical_preprocessing.md#the-inherited-finite-query-common-component), which identifies the additional Chiribella and Anshu–Landau–Liu sources.

### M28 — An exactly solvable retained-quantum endpoint

- **Central question:** What is optimal when the query is described only after the quantum references have been retained?
- **Understanding target:** Explain commuting conditional hypotheses, the independent false-pass distribution, uniform tie breaking and the exact success formula. Distinguish that endpoint from finite-copy query access.
- **Dependencies and story role:** M05, M12, M19 and M23–M27; compare the two models under the same ideal later information.
- **Conceptual connection:** Query tomography can approach the endpoint at fixed parameters, but is not granted as an efficient or finite-copy primitive.
- **Source pointers:** Watrous §2.3 and §3.1.2; [revealed-query endpoint](../science/revealed_query.md); [classical endpoint scope](../science/classical_preprocessing.md#edge-cases-and-scope).

### M29 — A resource-matched separation

- **Central question:** Which parameter regime demonstrates the value of retaining the supplied references?
- **Understanding target:** Explain the one-reference-copy comparison with a linear query-copy budget in sufficiently large dimension; contrast fixed-copy saturation with the logarithmic classical-copy necessity and the matched shadow upper comparator.
- **Dependencies and story role:** M19, M21 and M26–M28; connect quantum attainability, classical impossibility and known baselines into one operational statement.
- **Conceptual connection:** Matching supplied references and later information reveals a memory/chronology advantage without claiming an exponential total-sample or runtime improvement.
- **Source pointers:** Watrous §3.1.2 and §7.2.1 for the discrimination and random-state framework; [classical preprocessing loss](../science/interpretation.md#what-classical-preprocessing-loses); [growing budgets and baselines](../science/interpretation.md#growing-reference-budgets-and-matched-baselines); [related work](../references/RELATED_WORK.md).

### M30 — The complete scientific conclusion and its boundary

- **Central question:** What has this project established, and what would require a different theorem?
- **Understanding target:** Give a connected account of the multiclass finite-query frontier, sharp classical saturation and implementable scan, with correct attribution, input costs, dimension and chronology conditions. Identify why arbitrary libraries, mixed/noisy states, repeated reuse and runtime superiority remain outside the result.
- **Dependencies and story role:** M12–M29; synthesize the whole narrative rather than append an extra technical topic.
- **Conceptual connection:** Correct proofs, inherited tools, the surviving contribution, finite validation and scope qualifications are distinct parts of the scientific account.
- **Source pointers:** Watrous §2.1–§2.3, §3.1.2 and §7.1–§7.2 as the shared framework; [scientific route](../science/README.md); [scope and interpretation](../science/interpretation.md#what-follows-and-what-remains-outside-the-model); [attribution](../references/RELATED_WORK.md); [verification](../verification/README.md).
