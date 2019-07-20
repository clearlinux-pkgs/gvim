#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : gvim
Version  : 8.1.1717
Release  : 861
URL      : https://github.com/vim/vim/archive/v8.1.1717/vim-8.1.1717.tar.gz
Source0  : https://github.com/vim/vim/archive/v8.1.1717/vim-8.1.1717.tar.gz
Summary  : Vi Improved, a highly configurable, improved version of the vi text editor (with advanced features, such as a GUI)
Group    : Development/Tools
License  : LGPL-2.1 MIT
Requires: gvim-bin = %{version}-%{release}
Requires: gvim-data = %{version}-%{release}
Requires: gvim-license = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : buildreq-qmake
BuildRequires : desktop-file-utils
BuildRequires : elfutils-dev
BuildRequires : gpm-dev
BuildRequires : gtk3-dev
BuildRequires : gvfs-dev
BuildRequires : libXdmcp-dev
BuildRequires : libXpm-dev
BuildRequires : libXt-dev
BuildRequires : lua-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(xpm)
BuildRequires : pkgconfig(xt)
BuildRequires : python3-dev
BuildRequires : ruby
Patch1: 0001-fix-symlink-from-gvimdiff-and-gview.patch

%description
WHAT IS VIM?
Vim is a greatly improved version of the good old UNIX editor Vi.  Many new
features have been added: multi-level undo, syntax highlighting, command line
history, on-line help, spell checking, filename completion, block operations,
script language, etc.  There is also a Graphical User Interface (GUI)
available.  Still, Vi compatibility is maintained, those who have Vi "in the
fingers" will feel at home.  See "runtime/doc/vi_diff.txt" for differences with
Vi.

%package bin
Summary: bin components for the gvim package.
Group: Binaries
Requires: gvim-data = %{version}-%{release}
Requires: gvim-license = %{version}-%{release}

%description bin
bin components for the gvim package.


%package data
Summary: data components for the gvim package.
Group: Data

%description data
data components for the gvim package.


%package license
Summary: license components for the gvim package.
Group: Default

%description license
license components for the gvim package.


%prep
%setup -q -n vim-8.1.1717
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563637331
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure  --with-features=huge \
--with-tlib=ncurses \
--enable-gtk3-check \
--enable-cscope \
--enable-multibyte \
--enable-gui \
--enable-gui=gtk3 \
--enable-luainterp \
--enable-pythoninterp \
--enable-rubyinterp \
--enable-python3interp
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1563637331
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gvim
cp src/libvterm/LICENSE %{buildroot}/usr/share/package-licenses/gvim/src_libvterm_LICENSE
cp src/xdiff/COPYING %{buildroot}/usr/share/package-licenses/gvim/src_xdiff_COPYING
cp src/xpm/COPYRIGHT %{buildroot}/usr/share/package-licenses/gvim/src_xpm_COPYRIGHT
%make_install
## install_append content
mv %{buildroot}/usr/bin/vim %{buildroot}/usr/bin/gvim
rm -rf %{buildroot}/usr/share/vim/vim81
rm -rf %{buildroot}/usr/share/man
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/eview
%exclude /usr/bin/evim
%exclude /usr/bin/ex
%exclude /usr/bin/rgview
%exclude /usr/bin/rgvim
%exclude /usr/bin/rview
%exclude /usr/bin/rvim
%exclude /usr/bin/view
%exclude /usr/bin/vimdiff
%exclude /usr/bin/vimtutor
%exclude /usr/bin/xxd
/usr/bin/gview
/usr/bin/gvim
/usr/bin/gvimdiff
/usr/bin/gvimtutor

%files data
%defattr(-,root,root,-)
%exclude /usr/share/applications/vim.desktop
/usr/share/applications/gvim.desktop
/usr/share/icons/hicolor/48x48/apps/gvim.png
/usr/share/icons/locolor/16x16/apps/gvim.png
/usr/share/icons/locolor/32x32/apps/gvim.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gvim/src_libvterm_LICENSE
/usr/share/package-licenses/gvim/src_xdiff_COPYING
/usr/share/package-licenses/gvim/src_xpm_COPYRIGHT
