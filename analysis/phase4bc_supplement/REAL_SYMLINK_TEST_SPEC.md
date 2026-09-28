# Original real-link contract

Original test: test_context_engine.PacketTests.test_symlink_rejected. Source SHA-256: 7512546713e01db9e76f90c5bab121d8fba3b614ab1f3d3dbea25a1bbd69c3b6. Guard SHA-256: 5093064bc2a738b7a9f21a68bbc18532fae4321a0e9f9b9ac7ef3d735172268f. Parent architecture:63927844eaac94765a7a804ab128076a88cad6eac2f534b715b08b17c4e21606.

The unchanged method creates a real file symbolic link to an otherwise admissible synthetic document, redirects registry inclusion to that link, and requires build_packet to raise GuardError. The regular-file positive control must succeed. A junction, shortcut, copied file, mock, or outside-root-only rejection is not equivalent. The harness changes synthetic fixture placement only and imports frozen code read-only with bytecode disabled.
