#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bats
Version  : 0.4.0
Release  : 6
URL      : https://github.com/sstephenson/bats/archive/v0.4.0.tar.gz
Source0  : https://github.com/sstephenson/bats/archive/v0.4.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: bats-bin
Requires: bats-doc
Patch1: makefile.patch

%description
# Bats: Bash Automated Testing System
Bats is a [TAP](http://testanything.org)-compliant testing framework
for Bash. It provides a simple way to verify that the UNIX programs
you write behave as expected.

%package bin
Summary: bin components for the bats package.
Group: Binaries

%description bin
bin components for the bats package.


%package doc
Summary: doc components for the bats package.
Group: Documentation

%description doc
doc components for the bats package.


%prep
%setup -q -n bats-0.4.0
%patch1 -p1

%build
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bats
/usr/libexec/bats
/usr/libexec/bats-exec-suite
/usr/libexec/bats-exec-test
/usr/libexec/bats-format-tap-stream
/usr/libexec/bats-preprocess

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man7/*
