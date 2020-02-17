Name:           julius
Version:        1.3.0
Release:        1
Summary:        An open source re-implementation of Caesar III
License:        MIT
Group:          Games/Other
Url:            https://github.com/bvschaik/julius
Source0:	https://github.com/bvschaik/julius/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(sdl2)
BuildRequires:  cmake
BuildRequires:	pkgconfig(SDL2_mixer) 

%description
Julius is an open source re-implementation of Caesar III.

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
#---------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build
