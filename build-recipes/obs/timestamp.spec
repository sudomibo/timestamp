#
# spec file for package timestamp
#
# Copyright (c) 2025 SUSE Software Solutions
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           timestamp
Version:        main
Release:        0
Summary:        Just a simple 'date +%s' replacement for fun - nothing big and professional
License:        SUSE-Public-Domain
URL:            https://github.com/sudomibo/timestamp
Source:         main.tar.gz
BuildRequires:  clang-devel
BuildRequires:  make

%description
Just a simple 'date +%s' replacement for fun - nothing big and professional.

%prep
%setup -q -n %{name}-%{version}

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}

%changelog
* Mon Jun 30 2025 Mislav Bozicevic <mislav.bozicevic@suse.com>
- Initial release
