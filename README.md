
![image](https://github.com/g0dEngineer/AURA_AEON_HUMAN/blob/main/screenshots/aura_human_face_rig_eye_movement_movie__annotated.gif)

Youtube: https://youtu.be/kCWwG6jMMf8

# Who is AuraHuman?

# AuraHuman is Jamaica's 1st interactive 3d humanoid teaching assistant/artificial friend.

# Aura Human gives users from kids to uwi graduates, the chance to interact with a more humanized form of LLMs, and gets students hands dirty in setting up Aeon themselves.

# We want to bring Aeon interaction to more teachers' computers, Public Kiosks and Personal Student Laptops.

# AuraHuman is an improvement of God's Bennett's [Cryptosynth Aeon product/NFT human project](https://github.com/g0dEngineer/Cryptosynth).

AuraHuman Aeon is a reasonable use case given shortage of teachers.



![image](https://github.com/g0dEngineer/AURA_AEON_HUMAN/blob/main/screenshots/aura_human_face_rig_screenshot.png)



# Positive details about Aeon?

1. Aura Aeon responds quickly even on CPU mode. 

* Tested on i7600 and i5/i3 cpus, some configs with 128 mb dedicated vram to 6 gb dedicated.

2. Aura Aeon runs completely locally. 

* Aura Aeon Human doesn't need any APIs, because it runs on a quantized locally stored pretrained "brain" based on gpt2.

# Aura Human is open source.






# Setup AuraAeon (Warning somewhat long setup process in (2).)
Ensure You have blender 2.91, and Python37 installed.

1. Download AuraAeonHuman zip and extract.

1.b. The scene is too big for github, so download and place in extracted folder (1) above: https://drive.google.com/file/d/1frAod3JDvGD5rBhB2DN-wp3ka-PB3YR_/view

2. Follow python setup from my parent project; Cryptosynth: https://github.com/g0dEngineer/Cryptosynth#part-b---python-setup
   * Alternatively, you could download [my already prepared Blender 2.91 instance fully setup with the hacks and requirements](https://drive.google.com/file/d/1NH62ZbV0K82jCSXzHTwOgtRPeCYI5wmZ/view?usp=drive_link).

4. Open a new cmd, and set path as the blender instance of python 2.91.

	3.a: Example: path=C:\Program Files\Blender Foundation\Blender 2.91\2.91\python\bin
   
	3.b: Uninstall pywin32 if it exists. python -m pip uninstall pywin32
   
	3.c: Install pywin32:  python -m pip install pywin32. This enables pywintypes to be correct.
   
	3.d: Install pyttsx3:  python -m pip install pyttsx3. This enables playing of aigenerated sound files
   
	3.e: Install pygame:  python -m pip install pygame. This enables playing of ambience files
	
5. Prepare aura_human_blender_plugin.zip.
	i Extract, navigate to utils.py file, and change the tempdir portion that applies to your machine. "C:/Users/18765/"
 	ii Zip the plugin, ensure all files are in one folder. 
 	iii Now zip plugin data again. (Apologies for this flow. This ai model param could have been made into a customizable param hence requiring no re-zipping, like my working sound param in this plugin, maybe in a later update :)
 	iv Open blender > Edit > Preferences > Addons > Navigate to zip in aeon folder/addons.


7. At the plugin section, give AuraAeon a place to establish a working speech file directory, where speech is generated and converted to facial  expressions.

8. Install blender-rhubarb-lipsync-windows-3.0.1.zip. Don't extract, open blender > Edit > Preferences > Addons > Navigate to zip in aeon folder/addons.

9. Setup done. See usage below.


![image](https://github.com/g0dEngineer/AURA_AEON_HUMAN/blob/main/screenshots/aura_human_face_rig_screenshot_eye_bone.png)



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

c. 700 mb space.


![image](https://github.com/g0dEngineer/AURA_AEON_HUMAN/blob/main/screenshots/aura_human_face_rig_screenshot.png)


# Dev Stack, Background details for contributing to and improving Aeon
Fusion of several tech stacks

1. Hack: Custom blender3d 2.91 plugin to integrate standard py3.7 torch conversational pretrained large language ai model into blender ux
2. Tensorflow 2d Ai fake human generator, based on pretrained weights
3. Ai 2d photo to 3d model program (Aeon Human character)
4. Face it landmark + armature generator  (faceit-beta-v2.3.8 beta)
5. Core Animation Lucky Hack: (select model then armature, ctrl+p > automatic weights) Blender 2.91 native Automatic Weight generator. (Applied to face it landmark as alternative to face it binding, which lead to an error. Binding is needed to map animation armature/guide to character skin.)
6. Aeon custom mouth shapes made based on Rhubarb documentation guide as well as combination of hck (5) and (4): https://github.com/DanielSWolf/rhubarb-lip-sync#mouth-shapes
7. Python Text To Sound Generator 
8. Bind function via face it, so when rig moves, armature and bones move. Also enables Pose Lib creation which is fed to lipsynch rhubarb. Do faceitbind, then repeat hack 5. Bind only moves eyes. Hack 5 enables face/jaw/mouth movement.

Note [1] Bind will duplicate head, eyes etc. Move duplicates to a clone folder and hide/disable that folder.
Note [2] I bind with scale factor 1. A scale of 100, may make the mesh dissappear.

Note [3[ -Eyes won't move , neither teeth, tongue, unless the 3d objects are parented to respective armatures. 

Do the following.
My reminder written from memory for parenting eyes to eyes armature, teeth to teeth armature.: Select Mesh (origin to geom) > Shift + S > Cursor to Selected > Select Rig > Select Bonelayer > Select appropriate bone > Shift + S > Selected to Cursor > Select Mesh Again + Select Rig > Ctrl + P > Bone (Parent mesh, to rig)

Note, bug when parenting takes place, object/child scales up , and relocates top screen. Solution is to scale back to appropriate, and manually relocate. To make things easier use duplicate objects from "Note[1] binding..." earlier, colour duplicate separately, like a bright purple, to make rematching of child easier, as duplicate would stay in place with default size.

9. Hack for deletion of rouge bones: Some rouge bones caused animation to distort aeon human head very disturbingly. To fix this
   
I programmatically removed these bones. Why? These bones in edit mode dissapeared, despite bones being checked in overlay. 

See scripts : delete_rouge_bones.py and associated scripts in preprocessing_for_armature_weighting.py. You don't need to worry about these, as the scene was saved after deletion of these rouge bones.


