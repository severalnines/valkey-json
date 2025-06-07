# valkey-json.spec
Name: valkey-json
Version: 1.0.0
Release: 1%{?dist}
Summary: Valkey JSON module
License: BSD 3-Clause License
BuildArch: x86_64

%description
A C++ Valkey module that provides native JSON support.

%prep
# No prep needed

%build
# No build needed

%install
mkdir -p %{buildroot}/usr/lib/valkey
cp %{_sourcedir}/libjson.so %{buildroot}/usr/lib/valkey/

%files
%defattr(-,root,root,-)
/usr/lib/valkey/libjson.so