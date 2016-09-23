.PHONY: render all

render:
	blender --background scene.blend --python scene.py --render-output botimage --frame-start 0 --frame-end 12 --render-anim

animation.gif: render
	gm convert -delay 20 -loop 0 botimage*.png animation.gif

all: animation.gif
