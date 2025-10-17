%define major	3
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Name:		kgraphviewer
Version:	25.08.2
Release:	2
Summary:	A GraphViz dot graph viewer for Plasma
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/applications/graphics/kgraphviewer
Source0:	https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6IconThemes)

BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)

BuildRequires:	desktop-file-utils
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libcgraph)

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

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
%{_bindir}/kgraphviewer
%{_qtdir}/plugins/kf6/parts/kgraphviewerpart.so
%{_datadir}/applications/org.kde.kgraphviewer.desktop
%{_datadir}/config.kcfg/kgraphviewer_partsettings.kcfg
%{_datadir}/config.kcfg/kgraphviewersettings.kcfg
%{_datadir}/icons/hicolor/*/apps/kgraphviewer.png
%{_datadir}/metainfo/org.kde.kgraphviewer.appdata.xml
%{_datadir}/qlogging-categories6/kgraphviewer.categories

#----------------------------------------------------------------------------

%package -n	%{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains shared library for %{name}.

%files -n %{libname}
%{_libdir}/libkgraphviewer.so*

#----------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains development files for %{name}.

%files -n %{devname}
%{_includedir}/kgraphviewer
%{_libdir}/cmake/KGraphViewerPart
