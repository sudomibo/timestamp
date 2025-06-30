# timestamp

## Description
Just a simple `date +%s` replacement for fun - nothing big and professional. Project is used to experiment with packaging and build services.

## Build
To build, run `make` from the project directory.

## License
No rights reserved, released to the public domain.

## Quick Start on OBS
For the full tutorial and documenation see https://openbuildservice.org/files/manuals/obs-user-guide.pdf

Without further ado, and assuming you are running on openSUSE Tumbleweed, first add the `osc` tooling:

```bash
zypper addrepo https://download.opensuse.org/repositories/openSUSE:/Tools/openSUSE_Tumbleweed/openSUSE:Tools.repo
zypper refresh
zypper install osc build perl-libwww-perl perl-XML-Parser diffutils
groupadd --gid 399 abuild
useradd --system --uid 399 --gid abuild --home-dir /home/abuild --shell /bin/bash abuild
mkdir -p /home/abuild
chown abuild:abuild /home/abuild
usermod -a -G trusted abuild
``` 

To create the initial project and first release:
```bash
osc checkout home:mbozicevic
cd home\:mbozicevic/
osc mkpac timestamp
cd timestamp
wget https://github.com/sudomibo/timestamp/archive/refs/heads/main.zip #extract, and repack into a tar.gz
vi timestamp.spec # edit so that it matches https://github.com/sudomibo/timestamp/blob/main/build-recipes/obs/timestamp.spec
osc vc
osc add *.spec *.changes *.tar.gz
osc build --local-package
osc commit
osc buildlog openSUSE_Tumbleweed x86_64
```

