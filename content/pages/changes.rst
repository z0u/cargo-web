Change Log
##########

:slug: changes

This page summarises how each release differs from the previous one. For more details, see the `commit log`_ in the source code repository.

.. _commit log: https://github.com/oasakfu/cargo/commits/master

0.98
====

2014-02-16

- Upgraded Blender version to 2.69 fdcdd5e (2014-02-13).
- Improved interactions with the Ant.
- Improved texture of distant trees. Added park benches.
- Increased camera blur.
- Increased mouse sensitivity, and inverted y-axis to match other games.
- Fixed letterboxing for non-16:9 screens. Also added rounded corners.
- Fixed texture paths for splash screen (used to just be black).
- Various other minor improvements.

0.97
====

2013-12-16

- Fixed a couple of crasher bugs relating to using a camera from the wrong scene.

0.96
====

2013-12-15

- Updated documentation (readme files).

0.95
====

2013-12-08

- Controls info is shown the first time the game starts.
- Improved slug conversation after items have been found.
- Limiting vertical camera offset based on ceiling height; this improves camera behaviour when going through tunnels.
- Probable fix for missing libGLEW library on some flavours of GNU/Linux (upstream change; static linking).
- Probable fix for Python error when starting game on some flavours of GNU/Linux (upstream change; newer Python version in Blender) (FAILED).

0.94
====

2013-10-17

- Disabled resolution change on OS X. Native resolution is used instead. This ensures the game is playable, but now requires a faster graphics card.
- Using adaptive V-sync. Should run a little faster on low-end computers.
- Fixed video option page dismissal.

0.93
====

2013-10-14

- Added version number to menu screen and console output to make debugging easier.

0.92
====

This is a crash fix for Linux, incorporating `a fix in Blender`_.

.. _a fix in blender: http://developer.blender.org/rB94fdaa5d41ecc33f48bec6d2094e67f533a0e5de

0.91
====

First closed beta release, for Windows and GNU/Linux.

