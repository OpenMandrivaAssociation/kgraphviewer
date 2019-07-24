%define major	3
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Name:		kgraphviewer
Version:	2.4.3
Release:	1
Summary:	A GraphViz dot graph viewer for Plasma 5
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/applications/graphics/kgraphviewer
Source0:	https://download.kde.org/stable/kgraphviewer/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5IconThemes)

BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)

BuildRequires:	desktop-file-utils
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libcgraph)

Requires:	graphviz

%description
KGraphViewer is a Graphviz DOT graph file viewer. Graphs are commonly
used in scientific domains and particularly in computer science.

Features:

  o Zooming
  o Threaded loading of several graphs in tabs
  o Saving of the recent files list
  o Manual reload of files
  o Display of a bird-eye view of the graph
  o Moving of the graph by dragging
  o Full featured printing
  o Perfect drawing of all graphviz example graphs
  o Automaticaly choose dot for directed graphs and neato for undirected
  o Possibility to use an arbitrary layout algo as soon as it produces
    xdot format
  o Automatic reloading with user confirmation of (externaly) modified
    files (configurable)
  o Open new instances as new tabs in the old one (configurable)

%files -f %{name}.lang
%{_kde5_sysconfdir}/xdg/%{name}.categories
%{_kde5_bindir}/%{name}
%{_kde5_datadir}/kgraphviewerpart/
%{_kde5_applicationsdir}/org.kde.%{name}.desktop
%{_kde5_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_kde5_datadir}/metainfo/org.kde.lib%{name}.metainfo.xml
%{_kde5_datadir}/config.kcfg/*.kcfg
%{_kde5_iconsdir}/hicolor/*/*/%{name}.png
%{_qt5_plugindir}/kgraphviewerpart.so
%{_kde5_services}/%{name}*.desktop
%{_kde5_datadir}/kxmlgui5/%{name}/

#----------------------------------------------------------------------------

%package -n	%{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains shared library for %{name}.

%files -n %{libname}
%{_kde5_libdir}/lib%{name}.so.%{major}
%{_kde5_libdir}/lib%{name}.so.%{version}

#----------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains development files for %{name}.

%files -n %{devname}
%{_includedir}/%{name}/
%{_kde5_libdir}/libkgraphviewer.so
%{_kde5_libdir}/cmake/KGraphViewerPart/

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name} --with-html

