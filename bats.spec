#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bats
Version  : 1.4.1
Release  : 23
URL      : https://github.com/bats-core/bats-core/archive/v1.4.1/bats-core-1.4.1.tar.gz
Source0  : https://github.com/bats-core/bats-core/archive/v1.4.1/bats-core-1.4.1.tar.gz
Summary  : Bash Automated Testing System
Group    : Development/Tools
License  : MIT
Requires: bats-bin = %{version}-%{release}
Requires: bats-libexec = %{version}-%{release}
Requires: bats-license = %{version}-%{release}
Requires: bats-man = %{version}-%{release}
Patch1: makefile.patch

%description
Bats is a TAP-compliant testing framework for Bash.
It provides a simple way to verify that the UNIX programs you write behave as expected.
Bats is most useful when testing software written in Bash, but you can use it to test any UNIX program.

%package bin
Summary: bin components for the bats package.
Group: Binaries
Requires: bats-libexec = %{version}-%{release}
Requires: bats-license = %{version}-%{release}

%description bin
bin components for the bats package.


%package libexec
Summary: libexec components for the bats package.
Group: Default
Requires: bats-license = %{version}-%{release}

%description libexec
libexec components for the bats package.


%package license
Summary: license components for the bats package.
Group: Default

%description license
license components for the bats package.


%package man
Summary: man components for the bats package.
Group: Default

%description man
man components for the bats package.


%prep
%setup -q -n bats-core-1.4.1
cd %{_builddir}/bats-core-1.4.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1627083731
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
# From Arch Linux PKGBUILD...
TERM=linux bin/bats --tap test

%install
export SOURCE_DATE_EPOCH=1627083731
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bats
cp %{_builddir}/bats-core-1.4.1/LICENSE.md %{buildroot}/usr/share/package-licenses/bats/1c44d90b844121642b1219f25b6b8ea3240f8cb9
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/bats-core/formatter.bash
/usr/lib/bats-core/preprocessing.bash
/usr/lib/bats-core/semaphore.bash
/usr/lib/bats-core/test_functions.bash
/usr/lib/bats-core/tracing.bash
/usr/lib/bats-core/validator.bash

%files bin
%defattr(-,root,root,-)
/usr/bin/bats

%files libexec
%defattr(-,root,root,-)
/usr/libexec/bats-core/bats
/usr/libexec/bats-core/bats-exec-file
/usr/libexec/bats-core/bats-exec-suite
/usr/libexec/bats-core/bats-exec-test
/usr/libexec/bats-core/bats-format-cat
/usr/libexec/bats-core/bats-format-junit
/usr/libexec/bats-core/bats-format-pretty
/usr/libexec/bats-core/bats-format-tap
/usr/libexec/bats-core/bats-format-tap13
/usr/libexec/bats-core/bats-preprocess

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bats/1c44d90b844121642b1219f25b6b8ea3240f8cb9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bats.1
/usr/share/man/man7/bats.7
