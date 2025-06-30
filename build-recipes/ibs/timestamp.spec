#
# spec file for package timestamp
#
Name:		timestamp
Version:	1.0
Release:	%autorelease
Summary:	Just a simple 'date +%s' replacement for fun - nothing big and professional
License:	SUSE-Public-Domain
URL:		https://github.com/sudomibo/timestamp
BuildRequires:	clang-devel
BuildRequires:	make

%description
Just a simple 'date +%s' replacement for fun - nothing big and professional. Project is used to experiment with packaging and build services.

%prep
cp -rf %{_topdir}/SOURCES/%name-*/ .

%build
cd %name-*/
%make_build
cp %name ..

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%check

%files
%{_bindir}/%{name}

%changelog
* Fri Feb 28 2025 Mislav Bozicevic <mislav.bozicevic@suse.com>
- Initial release

