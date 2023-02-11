# Lsmith bridge

This is an stable-diffusion-webui extension to bypass txt2img generate to Lsmith running locally.
The bypass destination is a URL in the UI, so if you have a public server, you can use it.

Sampler is not yet supported (it will always be "euler_a"), because it was too much trouble to find out if Lsmith has a corresponding sampler. If you just want to give the name, you can rewrite "euler_a" in scripts/lsmithbridge.py to "p.sampler_name".

I don't intend to do much maintenance at the moment, so please use it by forking on your own. You can be the maintainer of this project.
