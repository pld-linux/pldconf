Summary:	PLD Linux Distribution configuration tool
Summary(pl):	Narzêdzie do konfiguracji Dystrybucji Linuksa PLD
Name:		pldconf
Version:	0.3.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.inf.sgsp.edu.pl/pub/PROGRAMY/PLD/RPM/%{name}_%{version}.tgz
# Source0-md5:	e8bb0023cc5a0400537360cf8114ae22
URL:		http://www.inf.sgsp.edu.pl/pub/PROGRAMY/PLD/
BuildRequires:	sed
Requires:	bash
Requires:	dml
Requires:	pciutils
Requires:	%{_bindir}/perl
Requires:	psutils
Requires:	sh-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define		_pcdatadir	%{_datadir}/%{name}

%description
It's a friendly tool for first-time users, it asks only a few
questions and uses an graphical user interface on an text terminal. It
lets you configure your graphic environment, network and startup manager.

%description -l pl
Narzêdzie jest przyjazne dla pocz±tkuj±cych u¿ytkowników, zadaje ma³o
pytañ i korzysta z graficznego interfejsu u¿ytkownika na terminalu
tekstowym. Pozwala miêdzy innymi na konfiguracjê ¶rodowiska
graficznego, sieci i menad¿era startu.

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
cp -r POMOC NET SYSINFO X BOOT autorzy.sh inne.sh poldek.sh win.pl printer.sh ustawienia.sh menu_user.sh install_dc.sh $RPM_BUILD_ROOT%{_pcdatadir}
install dml.conf $RPM_BUILD_ROOT%{_sysconfdir}
echo "PLDCONF_VERSION=%{version}" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/ustawienia
echo "PLDCONF_EDITOR=vim" >> $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/ustawienia

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%dir %{_pcdatadir}
%attr(755,root,root) %{_pcdatadir}/*.sh
%attr(755,root,root) %{_pcdatadir}/*.pl

%dir %{_pcdatadir}/BOOT
%attr(755,root,root) %{_pcdatadir}/BOOT/*.sh
%attr(755,root,root) %{_pcdatadir}/BOOT/*.pl
%{_pcdatadir}/BOOT/*.c
%{_pcdatadir}/BOOT/*.txt
%dir %{_pcdatadir}/BOOT/MBRS
%{_pcdatadir}/BOOT/MBRS/*.dd

%dir %{_pcdatadir}/NET
%attr(755,root,root) %{_pcdatadir}/NET/*.sh
%attr(755,root,root) %{_pcdatadir}/NET/*.pl
%dir %{_pcdatadir}/NET/NET_FILES/
%attr(755,root,root) %{_pcdatadir}/NET/NET_FILES/*.sh
%{_pcdatadir}/NET/NET_FILES/chat
%{_pcdatadir}/NET/NET_FILES/gui.part1
%{_pcdatadir}/NET/NET_FILES/gui.part2
%{_pcdatadir}/NET/NET_FILES/konfig
%{_pcdatadir}/NET/NET_FILES/lista_kart
%{_pcdatadir}/NET/NET_FILES/ppp-off
%{_pcdatadir}/NET/NET_FILES/ppp-on

%dir %{_pcdatadir}/POMOC
%{_pcdatadir}/POMOC/README*

%dir %{_pcdatadir}/SYSINFO
%attr(755,root,root) %{_pcdatadir}/SYSINFO/*.sh

%dir %{_pcdatadir}/X
%attr(755,root,root) %{_pcdatadir}/X/*.sh
%attr(755,root,root) %{_pcdatadir}/X/*.pl

%dir %{_pcdatadir}/X/KILLER_DESKTOP
%{_pcdatadir}/X/KILLER_DESKTOP/DirIcon
%{_pcdatadir}/X/KILLER_DESKTOP/hacker_bg.png
%{_pcdatadir}/X/KILLER_DESKTOP/ooo_red.png
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
%{_pcdatadir}/X/KILLER_DESKTOP/xfce4/settings/*

%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*
%{_sysconfdir}/dml.conf
