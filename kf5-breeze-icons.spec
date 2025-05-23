#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.116
%define		qtver		5.15.2
%define		kfname		breeze-icons

Summary:	Breeze icons theme
Summary(pl.UTF-8):	Motyw ikon Breeze
Name:		kf5-%{kfname}
Version:	5.116.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	0d6733dda53a1a3114967e4e2e8dee89
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpm-build(macros) >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
Requires:	%{name}-data = %{version}-%{release}
Obsoletes:	breeze-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
Breeze-icons is a freedesktop.org compatible icon theme.

%description -l pl.UTF-8
Breeze-icons to motyw ikon zgodny z freedesktop.org.

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
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
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
%dir %{_libdir}/cmake/KF5BreezeIcons
%{_libdir}/cmake/KF5BreezeIcons/KF5BreezeIconsConfig.cmake
%{_libdir}/cmake/KF5BreezeIcons/KF5BreezeIconsConfigVersion.cmake
