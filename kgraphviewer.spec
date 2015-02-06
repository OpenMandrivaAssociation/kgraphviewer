Name:		kgraphviewer
Version:	2.1.1
Release:	4
Summary:	A GraphViz dot graph viewer for KDE
License:	GPLv2+
Group:		Graphics
Url:		https://gna.org/projects/kgraphviewer
Source0:	https://api.opensuse.org/public/source/home:milianw:kdeapps/kgraphviewer/%{name}-%{version}.tar.gz
Patch0:		kgraphviewer-2.1.1-boost-1.50.patch
Requires:	graphviz
BuildRequires:	desktop-file-utils
BuildRequires:	boost-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	graphviz-devel
Requires:	graphviz

%description
KGraphViewer is user-friendly KDE application for viewing dot graphs
created for processing with GraphViz. Notable features provided include:

- loading of several graphs in tabs
- bird's-eye graph view
- zooming view
- simple printing
- context menu and toolbar for selecting layout algorithms
- session management

%files -f %{name}.lang
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*.so
%{_kde_applicationsdir}/*.desktop
%{_kde_appsdir}/*
%{_kde_datadir}/config.kcfg/*.kcfg
%{_kde_iconsdir}/*/*/*/*.png
%{_kde_services}/*.desktop

#--------------------------------------------------------------------

%define libkgraphviewer %mklibname kgraphviewer 3

%package -n %{libkgraphviewer}
Group:		Graphics
Summary:	Shared library for %{name}

%description -n %{libkgraphviewer}
This package contains shared library for %{name}.

%files -n %{libkgraphviewer}
%{_kde_libdir}/libkgraphviewer.so.*

#--------------------------------------------------------------------

%package devel
Group:		Graphics
Summary:	Development files for %{name}
Requires:	%{libkgraphviewer} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%files devel
%{_kde_libdir}/libkgraphviewer.so
%{_kde_includedir}/%{name}

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

desktop-file-install --vendor='' \
	--dir %{buildroot}%{_kde_datadir}/applications/kde4/ \
	--remove-key='Encoding' \
	--remove-category='Application' \
	--add-category='Science;Education' \
	%{buildroot}%{_kde_datadir}/applications/kde4/kgraphviewer.desktop \
	%{buildroot}%{_kde_datadir}/applications/kde4/kgrapheditor.desktop

%find_lang %{name} --with-html

