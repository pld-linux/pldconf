Summary:	PLD Linux configuration tool
Summary(pl):	Narzêdzie do konfiguracji Linuksa PLD
Name:		pldconf
Version:	0.3.9
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.inf.sgsp.edu.pl/pub/PROGRAMY/PLD/RPM/%{name}_%{version}.tgz
# Source0-md5:	d51fe61d8c92f6d67579e185218ea8f5
URL:		http://www.inf.sgsp.edu.pl/pub/PROGRAMY/PLD/
BuildRequires:	sed
Requires:	awk
Requires:	bash
Requires:	dml
Requires:	pciutils
Requires:	sed
Requires:	%{_bindir}/perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pcdatadir	%{_datadir}/%{name}

%description
This is a friendly tool for first-time users. It asks only a few
questions and makes use of a graphical user interface on a text
terminal. It makes possible for users to configure their graphic
environment, the network and startup manager and some other elements
of the system. There's only Polish interface available in the current
version.

%description -l pl
Narzêdzie jest przyjazne dla pocz±tkuj±cych u¿ytkowników, zadaje ma³o
pytañ i korzysta z graficznego interfejsu u¿ytkownika na terminalu
tekstowym. pldconf pozwala miêdzy innymi na konfiguracjê ¶rodowiska
graficznego, sieci, menad¿era startu. W chwili obecnej dostêpny jest
tylko interfejs w jêzyku polskim.

%prep
%setup -q -n %{name}_%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name},%{_pcdatadir}}

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
cp -r POMOC NET SYSINFO X BOOT DEVICE USER pldconf_functions win.pl {autorzy,inne,poldek,ustawienia,menu_user,install_pld}.sh $RPM_BUILD_ROOT%{_pcdatadir}

IPREFIX="/usr"
EXEC_PREFIX="${IPREFIX}/bin"
DATA_DIR="${IPREFIX}/share/pldconf"
CONF_DIR="/etc/pldconf"
CONF_FILE="${CONF_DIR}/ustawienia"

cat > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/ustawienia << EOF
export PLDCONF_PAGER=less
export FIX_ERRORS=1
export VERBOSE_MODE=1
export TIMEOUT_MODE=0
export SLEEP_TIME=2
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%dir %{_pcdatadir}
%{_pcdatadir}/pldconf_functions
%attr(755,root,root) %{_pcdatadir}/*.sh
%attr(755,root,root) %{_pcdatadir}/*.pl

%dir %{_pcdatadir}/BOOT
%attr(755,root,root) %{_pcdatadir}/BOOT/*.sh
%attr(755,root,root) %{_pcdatadir}/BOOT/*.pl
%{_pcdatadir}/BOOT/*.c
%{_pcdatadir}/BOOT/*.txt

%dir %{_pcdatadir}/NET
%attr(755,root,root) %{_pcdatadir}/NET/*.sh
%attr(755,root,root) %{_pcdatadir}/NET/*.pl
%dir %{_pcdatadir}/NET/NET_FILES/
%{_pcdatadir}/NET/NET_FILES/ppplicznik.conf
%{_pcdatadir}/NET/NET_FILES/cost

%dir %{_pcdatadir}/DEVICE
%attr(755,root,root) %{_pcdatadir}/DEVICE/*.sh
%dir %{_pcdatadir}/DEVICE/ALSA/
%attr(755,root,root) %{_pcdatadir}/DEVICE/ALSA/*.sh

%dir %{_pcdatadir}/POMOC
%{_pcdatadir}/POMOC/README*

%dir %{_pcdatadir}/USER
%attr(755,root,root) %{_pcdatadir}/USER/*.sh

%dir %{_pcdatadir}/SYSINFO
%attr(755,root,root) %{_pcdatadir}/SYSINFO/*.sh

%dir %{_pcdatadir}/X
%attr(755,root,root) %{_pcdatadir}/X/*.sh
%attr(755,root,root) %{_pcdatadir}/X/*.pl

%dir %{_pcdatadir}/X/KILLER_DESKTOP
%{_pcdatadir}/X/KILLER_DESKTOP/DirIcon
%{_pcdatadir}/X/KILLER_DESKTOP/hacker_bg.png
%{_pcdatadir}/X/KILLER_DESKTOP/ooo_red.png
%{_pcdatadir}/X/KILLER_DESKTOP/qcad_blue.png
%{_pcdatadir}/X/KILLER_DESKTOP/pldconf_red.png

%dir %{_pcdatadir}/X/KILLER_DESKTOP/Choices
%{_pcdatadir}/X/KILLER_DESKTOP/Choices/README

%dir %{_pcdatadir}/X/KILLER_DESKTOP/Choices/MIME-icons
%{_pcdatadir}/X/KILLER_DESKTOP/Choices/MIME-icons/*

%dir %{_pcdatadir}/X/KILLER_DESKTOP/Choices/MIME-types
%attr(755,root,root) %{_pcdatadir}/X/KILLER_DESKTOP/Choices/MIME-types/*

%dir %{_pcdatadir}/X/KILLER_DESKTOP/Choices/ROX-Filer/
%{_pcdatadir}/X/KILLER_DESKTOP/Choices/ROX-Filer/*

%dir %{_pcdatadir}/X/KILLER_DESKTOP/Defaults
%{_pcdatadir}/X/KILLER_DESKTOP/Defaults/*

%dir %{_pcdatadir}/X/KILLER_DESKTOP/xfce4
%dir %{_pcdatadir}/X/KILLER_DESKTOP/xfce4/settings
%{_pcdatadir}/X/KILLER_DESKTOP/xfce4/xfce4rc
%{_pcdatadir}/X/KILLER_DESKTOP/xfce4/keythemerc
%{_pcdatadir}/X/KILLER_DESKTOP/xfce4/settings/*

%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*
