Summary:	PLD Linux configuration tool
Summary(pl.UTF-8):	Narzędzie do konfiguracji Linuksa PLD
Name:		pldconf
Version:	0.3.16
Release:	4
License:	GPL
Group:		Applications/System
Source0:	http://www.inf.sgsp.edu.pl/pub/PROGRAMY/PLD/RPM/%{name}-%{version}.tar.gz
# Source0-md5:	f7a6a77db0642a83b5fc22b7a55e04d1
Patch0:		%{name}-help_utf8.patch
URL:		http://www.inf.sgsp.edu.pl/pub/PROGRAMY/PLD/
BuildRequires:	iconv
Requires:	bash
Requires:	dml
Requires:	gettext
Requires:	pciutils
Requires:	pci-database
Requires:	sed
Requires:	which
Requires:	%{_bindir}/perl
Requires:	less
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pcdatadir	%{_datadir}/%{name}

%description
This is a friendly tool for first-time users. It asks only a few
questions and makes use of a graphical user interface on a text
terminal. It makes possible for users to configure their graphic
environment, the network and startup manager and some other elements
of the system.

%description -l pl.UTF-8
Narzędzie jest przyjazne dla początkujących użytkowników, zadaje mało
pytań i korzysta z graficznego interfejsu użytkownika na terminalu
tekstowym. pldconf pozwala między innymi na konfigurację środowiska
graficznego, sieci, menadżera startu.

%prep
%setup -q
%patch0 -p1

%build
# added UTF-8 versions of help
for i in POMOC/README*txt
do
	iconv -f ISO-8859-2 -t UTF-8 $i > $i.pl_PL.UTF-8
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name},%{_pcdatadir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/locale/,%{_datadir}/doc/%{name}-%{version}}


find . | while read file
do
	if [ -f $file ]; then
		cat $file | \
			sed 's@/etc@%{_sysconfdir}@' | \
			sed 's@/usr/bin@%{_bindir}@' > tmp ; mv tmp $file
	fi
done

install pldconf $RPM_BUILD_ROOT%{_bindir}
cp -r BOOT DEVICES NET POMOC SYSINFO USER X pldconf_functions {autorzy,filesystems,inne,install_pld,menu_user,poldek_conf,poldek,template,user}.sh $RPM_BUILD_ROOT%{_pcdatadir}

cp -r locale/* $RPM_BUILD_ROOT%{_datadir}/locale
cp -r DOCS/* $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/

IPREFIX="/usr"
EXEC_PREFIX="${IPREFIX}/bin"
DATA_DIR="${IPREFIX}/share/pldconf"
CONF_DIR="/etc/pldconf"
CONF_FILE="${CONF_DIR}/ustawienia"

cat > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/ustawienia << EOF
export PLDCONF_PAGER=less
export ERRORS_HANDLE=ALWAYS_ASK
export VERBOSE_MODE=0
export TIMEOUT_MODE=0
export SLEEP_TIME=2
export X_MOUSE_PROTOCOL=auto
EOF

install X/gfx/pldconf.desktop $RPM_BUILD_ROOT%{_desktopdir}
install X/gfx/pldconf.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

# clean docdir
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc DOCS/README.hacking DOCS/README.i18n
%attr(755,root,root) %{_bindir}/*

%dir %{_pcdatadir}
%{_pcdatadir}/pldconf_functions
%attr(755,root,root) %{_pcdatadir}/*.sh

%dir %{_pcdatadir}/BOOT
%attr(755,root,root) %{_pcdatadir}/BOOT/*.sh
%{_pcdatadir}/BOOT/*.c

%dir %{_pcdatadir}/NET
%attr(755,root,root) %{_pcdatadir}/NET/*.sh
%dir %{_pcdatadir}/NET/NET_FILES
%{_pcdatadir}/NET/NET_FILES/cost

%dir %{_pcdatadir}/DEVICES
%attr(755,root,root) %{_pcdatadir}/DEVICES/*.sh
%dir %{_pcdatadir}/DEVICES/ALSA
%attr(755,root,root) %{_pcdatadir}/DEVICES/ALSA/*.sh
%dir %{_pcdatadir}/DEVICES/TV
%attr(755,root,root) %{_pcdatadir}/DEVICES/TV/*.sh
%{_pcdatadir}/DEVICES/TV/CARDLIST.bttv
%{_pcdatadir}/DEVICES/TV/CARDLIST.saa7134
%{_pcdatadir}/DEVICES/TV/CARDLIST.tuner

%dir %{_pcdatadir}/POMOC
%{_pcdatadir}/POMOC/README*

%dir %{_pcdatadir}/USER
%attr(755,root,root) %{_pcdatadir}/USER/*.sh

%dir %{_pcdatadir}/SYSINFO
%attr(755,root,root) %{_pcdatadir}/SYSINFO/*.sh

%dir %{_pcdatadir}/X
%attr(755,root,root) %{_pcdatadir}/X/*.sh

%dir %{_pcdatadir}/X/gfx
%{_pcdatadir}/X/gfx/*

%dir %{_pcdatadir}/X/archive
%{_pcdatadir}/X/archive/*

%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*

%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
