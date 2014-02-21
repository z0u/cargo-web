The Making of S. Cargo
######################

:slug: making-of-cargo
:summary: S. Cargo is an indy video game made in Melbourne, Australia. The game was developed over 5.5 years in the team's spare time (after work and school, and on weekends).

**Under construction**

*S. Cargo* is an indy video game made in Melbourne, Australia. The game was developed over 5.5 years in the team's spare time (after work and school, and on weekends). The first prototype was made back in 2002 when Alex was at uni. It was a simple game, with an unnamed snail that could crawl up walls and on the ceiling - but it lacked a story, so it was shelved while we studied, worked and went gallivanting around the world.

In 2008 the prototype was improved: crawling was made more realistic, and powerups were added. Crawling around as a snail was great fun, so the team sat down to create a story to support the game play.

Finally, the game was finished in early 2014.


Engine
======

*S. Cargo* was created using `Blender <http://blender.org>`_, the fantastic 3D modelling and animation tool. People use Blender to create `awesome still images <http://www.blenderguru.com/>`_ and short films. A little-known fact is that it also contains a game engine that allows you to bring your creations to life.

.. raw:: html

    <div class="figure">
      <a href="../static/images/Making-Screenshot-Snail.jpg" data-lightbox="blendergui"><img class="img-rounded" src="../static/images/Making-Screenshot-Snail-small.jpg"></a>
      <a href="../static/images/Making-Screenshot-CargoHouse.jpg" data-lightbox="blendergui"><img class="img-rounded" src="../static/images/Making-Screenshot-CargoHouse-small.jpg"></a>
    </div>

Blender games are created by adding logic (behaviours) to 3D objects. The logic can be seen in the screenshots above as the blocks and wires in the bottom half of the screen. Blender calls these *logic bricks*. They are instructions, like "When the user presses the *up arrow*, move the snail forward". Because *S. Cargo* is a complex game, extra behaviours were created using the `Python programming language <http://docs.python.org/3/tutorial/>`_. For example, this is part of the code that makes Cargo stick to the walls and ceilings::


    def orient(self):
        '''Adjust the orientation of the snail to match the nearest surface.'''
        # Use attitude object to apply root orientation.
        # Set property on object so it knows whether it's falling. This is used
        # to detect when to transition from S_FALLING to S_CRAWLING.
        self.touchedObject, self['nHit'] = self.attitude.apply()
    
        mat_rot = mathutils.Matrix.Rotation(self.bend_angle_fore, 3, 'Z')
        self.orient_segments(self.head_segments, mat_rot)
        mat_rot = mathutils.Matrix.Rotation(self.bend_angle_aft, 3, 'Z')
        self.orient_segments(self.tail_segments, mat_rot)
        self.armature.update()

Lots of custom logic was created in Python. In addition to code for sticking to the walls, there are functions for floating in water, power-ups, interactive conversations, and making the grass bend out of the way as Cargo crawls past.

Modding
=======

Do you want to make your own game? You can do it if you try! A great way to start is by modifying other games. *S. Cargo* is open source, so you can learn how it works by looking in the *assets* directory.

The **easiest way** to get started is to modify some textures in *assets/Textures/\*.png*. Just modify and save an image file in an editor such as `The GIMP <http://www.gimp.org/>`_, and your changes will appear the next time you play the game. Try changing the colour of the snail or her shell!

If you want to dig deeper you can edit the 3D *assets/\*.blend*  files with Blender, and the *assets/Scripts/\*.py*  files with a regular text editor, like `gedit <https://projects.gnome.org/gedit/>`_ on GNU+Linux or `Notepad++ <http://notepad-plus-plus.org/>`_ on Windows.


Credits
=======

*S. Cargo* was mostly created by Alex Fraser. But it couldn't have been done without the hard work of these wonderful people:

* Lara Micocki, Lev Lafayette and Jodie Fraser all had heaps of input into the story. Jodie also recorded sound effects for some characters, tested the game, and encouraged Alex to get out of the house occasionally.
* Junki Wano contributed lots of concept art, modelling and texturing. His unique style added a lot to the game. Junki has made other games; you can see more of his work in `his online portfolio <http://peacefield.weebly.com/>`_.
* Robert Leigh created *all the music* in the game. He's amazing! Check out his tunes at ....
* Mark Triggs and Campbell Barton helped with the programming and bug fixing. Mark made the interactive grass faster, and Campbell worked on Blender itself - fixing bugs in the game engine, and adding full-screen support in GNU+Linux.
* Ben Sturmfels programmed in-game messages. He also recorded many sound effects for the game, and laid the foundations for this whole web site.
* Ben Finney and Leigh Raymond recorded character voices for the slug and ant.
* Everyone listed above tested the game too, but the following people focussed on testing during development (alpha testing): Lachlan Kanaley, Damien Elmes and Caley Finn. They just couldn't get enough testing!

This game uses code and assets from other projects - made possible by free culture and free software licences. The following people unwittingly\* made great contributions to *S. Cargo*.

* `freesound.org <http://freesound.org/>`_ is a great place to get Creative Commons-licensed sound samples. The game uses sounds sampled and created by the following freesound.org users: 3bagbrew, FreqMan, HerbertBoland, Percy Duke, klakmart, aUREa, qubodup, thetruwu, nsp, kangaroovindaloo, ERH, Corsica_S, batchku, satrebor, gherat, ZeSoundResearchInc., CGEffex, UncleSigmund, dobroide.
* The Blender Foundation, in addition to creating Blender itself, have released lots of content (models, animation, etc.) under free licences. The Bird in *S. Cargo* was based on a model from the game `Yo Frankie! <http://www.yofrankie.org/>`_
* Ian McEwan from Ashima Arts wrote the GLSL noise generator that makes the grass blow in the wind.

\* Just joking - they knew what they were doing when they chose a free license.

