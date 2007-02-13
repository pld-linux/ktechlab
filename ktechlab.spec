# TODO:
#   fix desktop and %doc
#
Summary:	An integrated circuit simulator
Summary(pl.UTF-8):	Symulator układów elektronicznych
Name:		ktechlab
Version:	0.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://ktechlab.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	0cc2f2054f7906780c8580560f04b0ff
URL:		http://ktechlab.org/
BuildRequires:	kdelibs-devel >= 9:3.2
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTechlab is an IDE for electronic circuits and microcontrollers. It
can perform simulation a variety of components (logic, integrated,
linear, nonlinear and reactive), simulation and debugging of PIC
microcontrollers via gpsim, and comes with its own closely-linked and
complementary high level languages: FlowCode and Microbe.

%description -l pl.UTF-8
KTechlab jest środowiskiem do tworzenia obwodów elektronicznych i
mikrokontrolerów. Może symulować różne komponenty (logiczne, liniowe,
nieliniowe itp). Może także poprzez bibliotekę gpsim symulować pracę
mikrokontrolerów PIC.

%prep
%setup -q

%build
%configure \
	--with-qt-libraries=%{_libdir}

%{__make} \
        CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_datadir}/config.kcfg/%{name}.kcfg
%{_datadir}/apps/katepart/syntax/microbe.xml
%{_iconsdir}/*/*x*/*/*.png
%{_datadir}/mimelnk/application/*.desktop
%{_desktopdir}/%{name}.desktop
