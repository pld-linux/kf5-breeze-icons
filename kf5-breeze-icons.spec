#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.108
%define		qtver		5.15.2
%define		kfname		breeze-icons

Summary:	breeze icons
Name:		kf5-%{kfname}
Version:	5.108.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	64f1357904f7b4a854fff871bdccd7e1
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
Requires:	%{name}-data = %{version}-%{release}
Obsoletes:	breeze-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Breeze-icons is a freedesktop.org compatible icon theme.

%package data
Summary:	Data files for %{kfname}
Summary(pl.UTF-8):	Dane dla %{kfname}
Group:		X11/Applications
BuildArch:	noarch

%description data
Data files for %{kfname}.

%description data -l pl.UTF-8
Dane dla %{kfname}.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files data
%defattr(644,root,root,755)
%{_iconsdir}/breeze
%{_iconsdir}/breeze-dark

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KF5BreezeIcons/KF5BreezeIconsConfig.cmake
%{_libdir}/cmake/KF5BreezeIcons/KF5BreezeIconsConfigVersion.cmake
