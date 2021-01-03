Name:           julius
Version:        1.6.0
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
%{_datadir}/applications/com.github.bvschaik.julius.desktop
%{_datadir}/icons/hicolor/*/apps/com.github.bvschaik.julius.png
%{_datadir}/metainfo/com.github.bvschaik.julius.metainfo.xml
#---------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build
