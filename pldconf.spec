Summary:	PLD configuration tool
Summary(pl):	Narzêdzie do konfiguracji Linuksa PLD
Name:		pldconf
Version:	0.1.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.inf.sgsp.edu.pl/pub/PROGRAMY/PLD/%{name}_%{version}.tgz
URL:		http://www.inf.sgsp.edu.pl/pub/PROGRAMY/PLD/index.html
Requires:	bash
Requires:	dml
Requires:	perl
BuildRequires:	bash
BuildRequires:	dml
BuildRequires:	perl
BuildArch:      noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD configuration tool.

%description -l pl
Narzêdzie jest przyjazne dla pocz±tkuj±cych u¿ytkowników, zadaje ma³o
pytañ i korzysta z graficznego interfejsu u¿ytkownika.

%prep
%setup -q -n %{name}_%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}

find . | while read file
do
    if [ -f $file ]
    then
        cat $file | sed 's@/usr/local/share@%{_datadir}@' > tmp ; mv tmp $file
	cat $file | sed 's@/etc@%{_sysconfdir}@' > tmp ; mv tmp $file
        cat $file | sed 's@/usr/sbin@%{_sbindir}@' > tmp ; mv tmp $file
    fi
done

file=./install.sh
cat $file | sed 's@%{_datadir}@\$DESTDIR%{_datadir}@' > tmp ; mv tmp $file
cat $file | sed 's@%{_sysconfdir}@\$DESTDIR%{_sysconfdir}@' > tmp ; mv tmp $file
cat $file | sed 's@%{_sbindir}@\$DESTDIR%{_sbindir}@' > tmp ; mv tmp $file

chmod +x ./install.sh

DESTDIR=$RPM_BUILD_ROOT ./install.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/*.sh
%attr(755,root,root) %{_datadir}/%{name}/*.pl
%{_datadir}/%{name}/NET_FILES
%{_datadir}/%{name}/ROX_WMAKER
%attr(755,root,root)%{_datadir}/%{name}/POMOC_DML
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*
%{_sysconfdir}/dml.conf
