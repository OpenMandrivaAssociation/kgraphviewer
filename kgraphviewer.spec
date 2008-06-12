%define version 2.0.2
%define rel	2

Summary:	A GraphViz dot graph viewer for KDE
Name:		kgraphviewer
Version: 	%{version}
Release: 	%mkrel %{rel}
Source0: 	http://download.gna.org/kgraphviewer/%{name}-%version-kde4.0.80.tar.bz2
License: 	GPLv2+
Group: 		Graphics	 	
Url: 		https://gna.org/projects/kgraphviewer
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	graphviz
BuildRequires:	boost-devel
BuildRequires: 	kdepimlibs4-devel
BuildRequires:	desktop-file-utils
Obsoletes:      kde4-%name <= 2.0
Provides:       kde4-%name = %version

%description 
KGraphViewer is user-friendly KDE application for viewing dot graphs 
created for processing with GraphViz. Notable features provided include:

- loading of several graphs in tabs
- bird's-eye graph view
- zooming view
- simple printing
- context menu and toolbar for selecting layout algorithms
- session management

%post
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_libdir/kde4/*.so
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/*
%_kde_datadir/config.kcfg/*.kcfg
%_kde_iconsdir/*/*/*/*.png
%_kde_datadir/kde4/services/*.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version-kde4.0.80

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
cd build
%{makeinstall_std}
cd -

desktop-file-install --vendor='' \
	--dir %buildroot%_kde_datadir/applications/kde4/ \
	--remove-key='Encoding' \
	--remove-category='Application' \
	--add-category='Qt;KDE;Graphics;2DGraphics;Viewer' \
	%buildroot%_kde_datadir/applications/kde4/kgraphviewer.desktop \
	%buildroot%_kde_datadir/applications/kde4/kgrapheditor.desktop

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
