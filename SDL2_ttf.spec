%define major 0
%define api 2.0
%define libname %mklibname %{name}
%define oldlibname %mklibname %{name} 2.0 0
%define devname %mklibname %{name} -d
%global _disable_rebuild_configure 1
#define _disable_lto 1

Summary:	Simple DirectMedia Layer 2 - Sample TrueType Font Library
Name:		SDL2_ttf
Version:	2.22.0
Release:	1
License:	Zlib
Group:		System/Libraries
Url:		http://www.libsdl.org/projects/SDL_ttf/
Source0:	https://github.com/libsdl-org/SDL_ttf/releases/download/release-%{version}/SDL2_ttf-%{version}.tar.gz
#Patch0:		sdl2_ttf-2.0.12-mga-link.patch
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(freetype2)

%description
This is a sample library which allows you to use TrueType fonts in your SDL2
applications.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files -n %{devname}
%doc README.txt CHANGES.txt
%{_includedir}/SDL2/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/SDL2_ttf

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%configure \
	--enable-freetype \
	--disable-freetype-builtin \
	--enable-harfbuzz \
	--disable-harfbuzz-builtin

%build
%make_build

%install
%make_install
