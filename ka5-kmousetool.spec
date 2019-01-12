%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kmousetool
Summary:	kmousetool
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	78caf0a2b5c6041d0f16cd339c4442a3
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.46.0
BuildRequires:	kf5-kdoctools-devel >= 5.46.0
BuildRequires:	kf5-ki18n-devel >= 5.46.0
BuildRequires:	kf5-kiconthemes-devel >= 5.46.0
BuildRequires:	kf5-knotifications-devel >= 5.46.0
BuildRequires:	kf5-kxmlgui-devel >= 5.46.0
BuildRequires:	ninja
BuildRequires:	phonon-qt5-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMouseTool is a Linux-based KDE program. It clicks the mouse for you,
so you don't have to. It clicks the mouse for you, so you don't have
to. KMouseTool works with any mouse or pointing device.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmousetool
%{_desktopdir}/org.kde.kmousetool.desktop
%{_iconsdir}/hicolor/16x16/actions/kmousetool_off.png
%{_iconsdir}/hicolor/16x16/actions/kmousetool_on.png
%{_iconsdir}/hicolor/16x16/apps/kmousetool.png
%{_iconsdir}/hicolor/32x32/actions/kmousetool_off.png
%{_iconsdir}/hicolor/32x32/actions/kmousetool_on.png
%{_iconsdir}/hicolor/32x32/apps/kmousetool.png
%{_datadir}/kmousetool
%{_datadir}/metainfo/org.kde.kmousetool.appdata.xml
%lang(ca) %{_mandir}/ca/man1/kmousetool.1.*
%lang(de) %{_mandir}/de/man1/kmousetool.1.*
%lang(es) %{_mandir}/es/man1/kmousetool.1.*
%lang(et) %{_mandir}/et/man1/kmousetool.1.*
%lang(fr) %{_mandir}/fr/man1/kmousetool.1.*
%lang(it) %{_mandir}/it/man1/kmousetool.1.*
%lang(C) %{_mandir}/man1/kmousetool.1.*
%lang(nl) %{_mandir}/nl/man1/kmousetool.1.*
%lang(pt) %{_mandir}/pt/man1/kmousetool.1.*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kmousetool.1.*
%lang(sv) %{_mandir}/sv/man1/kmousetool.1.*
%lang(uk) %{_mandir}/uk/man1/kmousetool.1.*