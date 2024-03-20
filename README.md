
# Who is AuraHuman?

# AuraHuman is Jamaica's 1st interactive 3d humanoid teaching assistant/artificial friend.

# Aura Human gives users from kids to uwi graduates, the chance to interact with a more humanized form of LLMs, and gets students hands dirty in setting up Aeon themselves.

# We want to bring Aeon to interactive more teachers' computers, Public Kiosks and Personal Student Laptops.

# AuraHuman is an improvement of God's Bennett's [Cryptosynth Aeon product/NFT human project](https://github.com/g0dEngineer/Cryptosynth).





# Positive details about Aeon?

1. Aura Aeon responds quickly even on CPU mode. 

* Tested on i7600 and i5/i3 cpus, some configs with 128 mb dedicated vram to 6 gb dedicated.

2. Aura Aeon runs completely locally. 

* Aura Aeon Human doesn't need any APIs, because it runs on a quantized locally stored pretrained "brain" based on gpt2.

# Aura Human is open source.






# Setup AuraAeon (Warning somewhat long setup process in (2).)
Ensure You have blender 2.91, and Python37 installed.

1. Download AuraAeonHuman blender scene.

2. Follow python setup from my parent project; Cryptosynth: https://github.com/g0dEngineer/Cryptosynth#part-b---python-setup

3. Open a new cmd, and set path as the blender instance of python 2.91.

	3.a: Example: path=C:\Program Files\Blender Foundation\Blender 2.91\2.91\python\bin
   
	3.b: Uninstall pywin32 if it exists. python -m pip uninstall pywin32
   
	3.c: Install pywin32:  python -m pip install pywin32. This enables pywintypes to be correct.
   
	3.d: Install pyttsx3:  python -m pip install pyttsx3. This enables playing of aigenerated sound files
   
	3.e: Install pygame:  python -m pip install pygame. This enables playing of ambience files
	
5. Install aura_human_blender_plugin.zip. Don't extract, open blender > Edit > Preferences > Addons > Navigate to zip in aeon folder/addons.

6. At the plugin section, give AuraAeon a place to establish a working speech file directory, where speech is generated and converted to facial  expressions.

7. Install blender-rhubarb-lipsync-windows-3.0.1.zip. Don't extract, open blender > Edit > Preferences > Addons > Navigate to zip in aeon folder/addons.

8. Setup done. See usage below.






# Usage

1. Open scene "AURA_AEON_HUMAN.blend".

2. Press "I" to initialize Aura Aeon being. (Wait for "...initialization" message bottom left)
   Note: Apart from neural network initiali, this also pops up ambient music in what ever music program is default on your system.

3. Right click any empty grey area, and click top menu option, "AuraHuman Aeon Dialog".

4. Talk to Aura by typing some text in top field.

5. Press "T" so Aura can "think" up a response.

6. Wait less than a second for Aura to give a response. (Computer, i7 6700, gtx 1060, 6gig dedicated video memory or computer with same cpu, and 128mb dedicated video memory as cpu is mostly used.)

7. If Aeon doesn't speak, press "space" key. 

8. Press R to see what Aeon said in text form.


Note: For lipsync to work based on ai output speech, Aeon must be in Pose Mode. Ensure program stays in default Pose mode shipped with Aeon scane.



# Computer Requirements

Tested on:
a. i7 6700, gtx 1060, 6 gig dedicated video memory

b. i7600, integrated graphics chip, 128mb dedicated video memory. Response time is just about the same, as CPU is mostly used. 

Also runs on i5 and i3, with around 6gb system ram, and 128mb dedicated video ram.





# Dev Stack
Fusion of several tech stacks

1. Hack: Custom blender3d 2.91 plugin to integrate standard py3.7 torch conversational pretra large language ai model into blender ux
2. Tensorflow 2d Ai fake human generator, based on pretrained weights
3. Ai 2d photo to 3d model program (Aeon Human character)
4. Face it landmark + armature generator  (faceit-beta-v2.3.8 beta)
5. Core Animation Lucky Hack: (select model then armature, ctrl+p > automatic weights) Blender 2.91 native Automatic Weight generator. (Applied to face it landmark as alternative to face it binding, which lead to an error. Binding is needed to map animation armature/guide to character skin.)
6. Aeon custom mouth shapes made based on Rhubarb documentation guide as well as combination of hck (5) and (4): https://github.com/DanielSWolf/rhubarb-lip-sync#mouth-shapes
7. Python Text To Sound Generator 
8. Bind function via face it, so when rig moves, armature and bones move. Also enables Pose Lib creation which is fed to lipsynch rhubarb. Do faceitbind, then repeat hack 5. Bind only moves eyes. Hack 5 enables face/jaw/mouth movement.

Note [1] Bind will dupliocate head, eyes etc. Move duplicates to a clone folder and hide/disable that folder.
Note [2] I bind with scale factor 1. 100will dissapear the mesh.

Note [3[ -Eyes won't move , neither teeth, tounge, unless the 3d objects are parented to respective armatures. Do the following.
My reminder written from memory for parenting eyes to eyes armature, teeth to teeth armature.: Select Mesh (origin to geom) > Shift + S > Cursor to Selected > Select Rig > Select Bonelayer > Select appropriate bone > Shift + S > Selected to Cursor > Select Mesh Again + Select Rig > Ctrl + P > Bone (Parent mesh, to rig)

Note, bug when parenting takes place, object/child scales up , and relocates top screen. Solution is to scale backto appropriate, and manually relocate. To make things easier duplicae object before process, colour duplicate separately, like a bright purple, to make rematching of child easier, as duplicate would stay in place with default size.

9. Hack for deletion of rouge bones: Some rouge bones caused animation to distort aeon human head very disturbingly. To fix this
I programmatically removed these bones. Why? These bones in edit mode dissapeared, despite bones being checkedin overlay. See
scripts : delete_rouge_bones.py and associated scripts in preprocessing_for_armature_weighting.py. You don't need to worry about these, as the scene was saved after deletion of these rouge bones.


