# Phase 4BE-C checkpoint reconciliation

Final classification: `CHECKPOINT_RECONCILED_PHASE4BE_RECOVERY_BLOCKED`.

The original checkpoint generator recursively scanned the entire project. Its saved 152 canonical PDFs comprised 112 registered corpus sources and 40 operational/private PDF copies; five archived exact duplicates brought the total to 157. The drifted pair was preserved byte for byte, and isolated replay of the original generator over its checkpoint-era paths reproduced the recorded scientific state and issue set. The exact invoking writer remains unknown. Six more operational copies appeared after that checkpoint.

The repaired scanner uses twelve manifest-supported corpus roots and handles `99_Duplicates` separately. Its candidate and installed checkpoints report 112 canonical, five archived duplicates, 37 structural passes, 75 pending, zero source verified, zero promoted, and no issues. All 112 registered source hashes and the five duplicate hashes match. B02–B08 remain untouched in Phase 4BE authority. Independent Stage A technical review returned `PASS_WITH_LIMITATIONS`, and the live checkpoint pair was installed from validated candidates with exact readback.

Fresh Phase 4BE recovery preflight checked 17,245 protected baseline files and 189 external parent pins. One additional protected drift blocks continuation: `scripts/__pycache__/summary_state.cpython-312.pyc` was rewritten when the scanner regression test imported the repaired module. Its exact changed bytes are preserved under `forensic/`; the baseline bytes could not be recovered. The cache change is absent from the authorized external changeset. Independent review confirmed that this is a blocking authorization gap under the recovery rules. No Phase 4BE recovery event, preparation commit, freeze, B02 scientific access, or Lane B activity followed.

Next operation requires explicit reconciliation authority for that cache artifact or exact baseline restoration, followed by a new full recovery preflight.
