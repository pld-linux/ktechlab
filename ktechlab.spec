Summary:	An integrated circuit simulator
Summary(pl):	Symulator uk³adów elektronicznych
Name:		ktechlab
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ktechlab.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	0cc2f2054f7906780c8580560f04b0ff
URL:		http://ktechlab.org/
BuildRequires:	kdelibs-devel >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTechlab is an IDE for electronic circuits and microcontrollers. It
can perform simulation a variety of components (logic, integrated,
linear, nonlinear and reactive), simulation and debugging of PIC
microcontrollers via gpsim, and comes with its own closely-linked and
complementary high level languages: FlowCode and Microbe.

%description -l pl
KTechlab jest ¶rodowiskiem do tworzenia obwodów elektronicznych i
mikrokontrolerów. Mo¿e symulowaæ ró¿ne komponenty (logiczne, liniowe,
nieliniowe itp). Mo¿e tak¿e poprzez bibliotekê gpsim symulowaæ pracê
mikrokontrolerów PIC.

%prep
%setup -q

%build
%configure

%{__make} \
        CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_datadir}/applnk/Development/ktechlab.desktop $RPM_BUILD_ROOT%{_desktopdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc %{_datadir}/doc/HTML/en/%{name}/*
%{_datadir}/apps/%{name}
%{_datadir}/config.kcfg/%{name}.kcfg
%{_datadir}/apps/katepart/syntax/microbe.xml
%{_iconsdir}/*/*x*/*/*.png
%{_datadir}/mimelnk/application/*.desktop
%{_desktopdir}/%{name}.desktop
