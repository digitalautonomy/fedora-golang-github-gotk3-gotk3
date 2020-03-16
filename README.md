To fix: To build you need to manually clone and generate the tar.gz expected by the spec file.
Spec files uploaded to Fedora's repo auto download the source code. I would fix this later.

```
wget https://github.com/gotk3/gotk3/archive/v0.4.0.zip
unzip v0.4.0.zip 
rm -rf v0.4.0.zip 
tar zcf gotk3-0.4.0.tar.gz gotk3-0.4.0/
```

To build this package you would need to install the `glib2-devel, cairo-devel, gtk3-devel` packages.

Building the package:
```
fedpkg --release f31 local
```