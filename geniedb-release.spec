Name:           geniedb-release       
Version:        1
Release:        1
Summary:        Packages for GenieDB

Group:          System Environment/Base 

URL:            http://www.geniedb.com/
Source:        GenieDB.repo	
License:	Propietary

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
Requires:      redhat-release >=  %{version} 
Conflicts:     fedora-release

%description
This package contains the GenieDB repository configuration for yum and up2date.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .

%build


%install
rm -rf $RPM_BUILD_ROOT

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*

%changelog
* Thu Jul 12 2012 GenieDB Ltd. <tech@geniedb.com> - 1-1
- Initial Package
