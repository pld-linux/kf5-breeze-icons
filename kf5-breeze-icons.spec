%define		kdeframever	5.84
%define		qtver		5.9.0
%define		kfname		breeze-icons

Summary:	breeze icons
Name:		kf5-%{kfname}
Version:	5.84.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	3fe1d14bc1112b0bb7141c1af6c74d7b
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
Obsoletes:	breeze-icon-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Breeze-icons is a freedesktop.org compatible icon theme.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/breeze
%{_iconsdir}/breeze-dark
