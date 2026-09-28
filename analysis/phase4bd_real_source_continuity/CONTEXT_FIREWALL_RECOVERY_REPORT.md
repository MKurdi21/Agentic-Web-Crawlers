# Recovery context firewall

The worker is a fresh deterministic subprocess with a closed input header: exact approved packet, source/report identity, size, stage, context ID and wrapper hash, followed by the authorized current PDF bytes. Recovery narratives and coordinator history are never serialized into this input. Unknown header keys fail. It inherits operating-system permissions and environment; this is not an OS sandbox or independent human review.

The separate-context packet reviewer inspected exact packet and wrapper bytes and returned SEMANTIC_CONTEXT_CLEAN. Only B01 and its report ID in two current-binding fields receive the narrowly reviewed identity exception. Tests 24–25 reject injected historical narrative and a B01 identifier in the content body. Inherited context tests cover other forbidden examples and historical leakage. Static scanning and model review have detection limits; exact reconstruction prevents later contextual additions rather than claiming universal paraphrase detection.

Known runtime hardening limitations are preserved in the protocol and independent review. No diagnostic reviewer serves as a scientific validation worker. B02–B08 never enter worker source delivery.
