#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: f35655a
#
%define keepstatic 1
Name     : gvim
Version  : 9.1.0847
Release  : 4173
URL      : https://github.com/vim/vim/archive/v9.1.0847/vim-9.1.0847.tar.gz
Source0  : https://github.com/vim/vim/archive/v9.1.0847/vim-9.1.0847.tar.gz
Summary  : A highly configurable, improved version of the vi text editor (Graphical VIM)
Group    : Development/Tools
License  : LGPL-2.1 MIT Python-2.0
Requires: gvim-bin = %{version}-%{release}
Requires: gvim-data = %{version}-%{release}
Requires: gvim-license = %{version}-%{release}
Requires: vim
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : desktop-file-utils
BuildRequires : elfutils-dev
BuildRequires : gpm-dev
BuildRequires : gtk3-dev
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-fix-symlink-from-gvimdiff-and-gview.patch

%description
GVim is a highly configurable text editor for efficiently creating and changing
any kind of text. It is included as "vi" with most UNIX systems and with Apple
OS X. Among its features are: persistent, multi-level undo tree; extensive
plugin system; support for hundreds of programming languages and file formats;
powerful search and replace; integrates with many tools.

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
%setup -q -n vim-9.1.0847
cd %{_builddir}/vim-9.1.0847
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731023533
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
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
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1731023533
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gvim
cp %{_builddir}/vim-%{version}/runtime/pack/dist/opt/editorconfig/LICENSE.PSF %{buildroot}/usr/share/package-licenses/gvim/7c0b791b76ecfa9bbe4c5d6ba252aeb5ad175b04 || :
cp %{_builddir}/vim-%{version}/src/libvterm/LICENSE %{buildroot}/usr/share/package-licenses/gvim/9979f112bdecefd99762f24f6af76972c2a3a1a6 || :
cp %{_builddir}/vim-%{version}/src/xdiff/COPYING %{buildroot}/usr/share/package-licenses/gvim/65c71b7ff77a59a32247d83a528728637263c1b5 || :
cp %{_builddir}/vim-%{version}/src/xpm/COPYRIGHT %{buildroot}/usr/share/package-licenses/gvim/553dde2683f711f77fe79504be0429256223469d || :
export GOAMD64=v2
GOAMD64=v2
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/eview
rm -f %{buildroot}*/usr/bin/evim
rm -f %{buildroot}*/usr/bin/ex
rm -f %{buildroot}*/usr/bin/rgview
rm -f %{buildroot}*/usr/bin/rgvim
rm -f %{buildroot}*/usr/bin/rview
rm -f %{buildroot}*/usr/bin/rvim
rm -f %{buildroot}*/usr/bin/view
rm -f %{buildroot}*/usr/bin/vimdiff
rm -f %{buildroot}*/usr/bin/vimtutor
rm -f %{buildroot}*/usr/bin/xxd
rm -f %{buildroot}*/usr/share/applications/vim.desktop
rm -f %{buildroot}*/usr/share/icons/hicolor/48x48/apps/gvim.png
rm -f %{buildroot}*/usr/share/icons/locolor/16x16/apps/gvim.png
rm -f %{buildroot}*/usr/share/icons/locolor/32x32/apps/gvim.png
rm -f %{buildroot}*/usr/share/man/man1/eview.1
rm -f %{buildroot}*/usr/share/man/man1/evim.1
rm -f %{buildroot}*/usr/share/man/man1/ex.1
rm -f %{buildroot}*/usr/share/man/man1/gview.1
rm -f %{buildroot}*/usr/share/man/man1/gvim.1
rm -f %{buildroot}*/usr/share/man/man1/gvimdiff.1
rm -f %{buildroot}*/usr/share/man/man1/rgview.1
rm -f %{buildroot}*/usr/share/man/man1/rgvim.1
rm -f %{buildroot}*/usr/share/man/man1/rview.1
rm -f %{buildroot}*/usr/share/man/man1/rvim.1
rm -f %{buildroot}*/usr/share/man/man1/view.1
rm -f %{buildroot}*/usr/share/man/man1/vim.1
rm -f %{buildroot}*/usr/share/man/man1/vimdiff.1
rm -f %{buildroot}*/usr/share/man/man1/vimtutor.1
rm -f %{buildroot}*/usr/share/man/man1/xxd.1
rm -f %{buildroot}*/usr/share/man/*/man1/eview.1
rm -f %{buildroot}*/usr/share/man/*/man1/evim.1
rm -f %{buildroot}*/usr/share/man/*/man1/ex.1
rm -f %{buildroot}*/usr/share/man/*/man1/gview.1
rm -f %{buildroot}*/usr/share/man/*/man1/gvim.1
rm -f %{buildroot}*/usr/share/man/*/man1/gvimdiff.1
rm -f %{buildroot}*/usr/share/man/*/man1/rgview.1
rm -f %{buildroot}*/usr/share/man/*/man1/rgvim.1
rm -f %{buildroot}*/usr/share/man/*/man1/rview.1
rm -f %{buildroot}*/usr/share/man/*/man1/rvim.1
rm -f %{buildroot}*/usr/share/man/*/man1/view.1
rm -f %{buildroot}*/usr/share/man/*/man1/vim.1
rm -f %{buildroot}*/usr/share/man/*/man1/vimdiff.1
rm -f %{buildroot}*/usr/share/man/*/man1/vimtutor.1
rm -f %{buildroot}*/usr/share/man/*/man1/xxd.1
## install_append content
mv %{buildroot}/usr/bin/vim %{buildroot}/usr/bin/gvim
rm -rf %{buildroot}/usr/share/vim/vim8*
rm -rf %{buildroot}/usr/share/vim/vim9*
rm -rf %{buildroot}/usr/share/man
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gview
/usr/bin/gvim
/usr/bin/gvimdiff
/usr/bin/gvimtutor

%files data
%defattr(-,root,root,-)
/usr/share/applications/gvim.desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gvim/553dde2683f711f77fe79504be0429256223469d
/usr/share/package-licenses/gvim/65c71b7ff77a59a32247d83a528728637263c1b5
/usr/share/package-licenses/gvim/7c0b791b76ecfa9bbe4c5d6ba252aeb5ad175b04
/usr/share/package-licenses/gvim/9979f112bdecefd99762f24f6af76972c2a3a1a6
