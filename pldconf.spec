Summary:	PLD Linux Distribution configuration tool
Summary(pl):	Narzêdzie do konfiguracji Dystrybucji Linuksa PLD
Name:		pldconf
Version:	0.2.0
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://www.inf.sgsp.edu.pl/pub/PROGRAMY/PLD/%{name}_%{version}.tgz
URL:		http://www.inf.sgsp.edu.pl/pub/PROGRAMY/PLD/index.html
BuildRequires:	bash
BuildRequires:	dml
BuildRequires:	%{_bindir}/perl
Requires:	bash
Requires:	dml
Requires:	%{_bindir}/perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's friendly tool for first-time users, it ask only few questions and
uses graphical user interface at text terminal. It lets configure
graphics environment, network and startup manager.

%description -l pl
Narzêdzie jest przyjazne dla pocz±tkuj±cych u¿ytkowników, zadaje ma³o
pytañ i korzysta z graficznego interfejsu u¿ytkownika na terminalu
tekstowym. Pozwala miêdzy innymi na konfiguracjê ¶rodowiska graficznego,
sieci i menad¿era startu.

%prep
%setup -q -n %{name}_%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir}}

find . | while read file
do
    if [ -f $file ]
    then
        cat $file | sed 's@/usr/local/share@%{_datadir}@' > tmp ; mv tmp $file
	cat $file | sed 's@/etc@%{_sysconfdir}@' > tmp ; mv tmp $file
        cat $file | sed 's@/usr/sbin@%{_sbindir}@' > tmp ; mv tmp $file
    fi
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
cp pldconf $RPM_BUILD_ROOT%{_sbindir}
cp -r POMOC NET SYSINFO X BOOT autorzy.sh inne.sh poldek.sh win.pl ustawienia.sh $RPM_BUILD_ROOT%{_datadir}/%{name}
cp dml.conf $RPM_BUILD_ROOT%{_sysconfdir}/
echo PLDCONF_EDITOR=vim > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/ustawienia

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/*.sh
%attr(755,root,root) %{_datadir}/%{name}/*.pl
%attr(755,root,root)%{_datadir}/%{name}/POMOC_DML
%{_datadir}/%{name}/NET_FILES
%{_datadir}/%{name}/ROX_WMAKER
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*
%{_sysconfdir}/dml.conf
