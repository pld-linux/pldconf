Summary:	PLD Linux configuration tool
Summary(pl):	Narzêdzie do konfiguracji Linuksa PLD
Name:		pldconf
Version:	0.3.13
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://www.inf.sgsp.edu.pl/pub/PROGRAMY/PLD/RPM/%{name}-%{version}.tar.gz
# Source0-md5:	f1d218f3c49cf4c81f5be29700a1f3af
URL:		http://www.inf.sgsp.edu.pl/pub/PROGRAMY/PLD/
BuildRequires:	sed
Requires:	bash
Requires:	dml
Requires:	gettext
Requires:	pciutils
Requires:	sed
Requires:	which
Requires:	%{_bindir}/perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pcdatadir	%{_datadir}/%{name}

%description
This is a friendly tool for first-time users. It asks only a few
questions and makes use of a graphical user interface on a text
terminal. It makes possible for users to configure their graphic
environment, the network and startup manager and some other elements
of the system.

%description -l pl
Narzêdzie jest przyjazne dla pocz±tkuj±cych u¿ytkowników, zadaje ma³o
pytañ i korzysta z graficznego interfejsu u¿ytkownika na terminalu
tekstowym. pldconf pozwala miêdzy innymi na konfiguracjê ¶rodowiska
graficznego, sieci, menad¿era startu.

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name},%{_pcdatadir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/locale/,%{_datadir}/doc/%{name}-%{version}}


find . | while read file
do
    if [ -f $file ]
    then
	cat $file | \
		sed 's@/etc@%{_sysconfdir}@' | \
		sed 's@/usr/bin@%{_bindir}@' > tmp ; mv tmp $file
    fi
done

install pldconf $RPM_BUILD_ROOT%{_bindir}
cp -r BOOT DEVICES NET POMOC SYSINFO USER X pldconf_functions {autorzy,filesystems,inne,install_pld,menu_user,poldek_conf,poldek,template,user,ustawienia}.sh $RPM_BUILD_ROOT%{_pcdatadir}

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

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc DOCS/README.hacking DOCS/README.i18n DOCS/TODO
%attr(755,root,root) %{_bindir}/*

%dir %{_pcdatadir}
%{_pcdatadir}/pldconf_functions
%attr(755,root,root) %{_pcdatadir}/*.sh

%dir %{_pcdatadir}/BOOT
%attr(755,root,root) %{_pcdatadir}/BOOT/*.sh
%{_pcdatadir}/BOOT/*.c

%dir %{_pcdatadir}/NET
%attr(755,root,root) %{_pcdatadir}/NET/*.sh
%dir %{_pcdatadir}/NET/NET_FILES/
%{_pcdatadir}/NET/NET_FILES/ppplicznik.conf
%{_pcdatadir}/NET/NET_FILES/cost

%dir %{_pcdatadir}/DEVICES
%attr(755,root,root) %{_pcdatadir}/DEVICES/*.sh
%dir %{_pcdatadir}/DEVICES/ALSA/
%attr(755,root,root) %{_pcdatadir}/DEVICES/ALSA/*.sh
%dir %{_pcdatadir}/DEVICES/TV/
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
%{_pcdatadir}/X/gfx/README

%dir %{_pcdatadir}/X/archive
%{_pcdatadir}/X/archive/*

%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*

%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
