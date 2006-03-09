Summary:	Utilities for Synaptics touchpad
Summary(pl):	Narzêdzia do touchpada Synaptics
Name:		xorg-app-synaptics
Version:	0.14.4
Release:	0.1
Epoch:		0
License:	GPL
Group:		X11/Applications
Source0:	http://w1.894.telia.com/~u89404340/touchpad/files/synaptics-%{version}.tar.bz2
# Source0-md5:	ae9aef7a146346fbfc7edfdd63cdd273
URL:		http://w1.894.telia.com/~u89404340/touchpad/
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	perl-base
Obsoletes:	X11-synaptics
Requires:	xorg-driver-input-synaptics = %{epoch}:%{version}-%{release}
ExcludeArch:	sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for Synaptics touchpad.

%description -l pl
Narzêdzia do touchpada Synaptics.

%package -n xorg-driver-input-synaptics
Summary:	XOrg/XFree86 input driver for Synaptics and ALPS touchpads
Summary(pl):	Sterownik wej¶ciowy XOrg/XFree86 do touchpadów Synaptics oraz ALPS
Group:		X11/Libraries
Obsoletes:	XFree86-input-synaptics
Obsoletes:	X11-input-synaptics

%description -n xorg-driver-input-synaptics
XFree86 input driver for Synaptics touchpad.

%description -n xorg-driver-input-synaptics -l pl
Sterownik wej¶ciowy XFree86 do touchpada Synaptics.

%prep
%setup -q -n synaptics-%{version}

%build
%{__make} clean all \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	LIBDIR=%{_lib}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/modules/input}

install synclient syndaemon $RPM_BUILD_ROOT%{_bindir}
install manpages/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install synaptics_drv.o $RPM_BUILD_ROOT%{_libdir}/modules/input

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files -n xorg-driver-input-synaptics
%defattr(644,root,root,755)
%doc COMPATIBILITY INSTALL NEWS README* TODO
%lang(de) %doc INSTALL.DE
%lang(fr) %doc INSTALL.FR
%attr(755,root,root) %{_libdir}/modules/input/*.o
