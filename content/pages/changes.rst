Change Log
##########

:slug: changes

This page describes how each release differs from the previous one.

0.97
====

- Fixed a couple of crasher bugs relating to using a camera from the wrong scene.

0.96
====

- Updated documentation (readme files).

0.95
====

- Controls info is shown the first time the game starts.
- Improved slug conversation after items have been found.
- Limiting vertical camera offset based on ceiling height; this improves camera behaviour when going through tunnels.
- Probable fix for missing libGLEW library on some flavours of GNU/Linux (upstream change; static linking).
- Probable fix for Python error when starting game on some flavours of GNU/Linux (upstream change; newer Python version in Blender) (FAILED).

0.94
====

- Disabled resolution change on OS X. Native resolution is used instead. This ensures the game is playable, but now requires a faster graphics card.
- Using adaptive V-sync. Should run a little faster on low-end computers.
- Fixed video option page dismissal.

0.93
====

- Added version number to menu screen and console output to make debugging easier.

0.92
====

This is a crash fix for Linux, incorporating [a fix in Blender](http://developer.blender.org/rB94fdaa5d41ecc33f48bec6d2094e67f533a0e5de).

0.91
====

First closed beta release, for Windows and GNU/Linux.

