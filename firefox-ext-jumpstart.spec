%define srcname new_tab_jumpstart

Summary:	New Tab JumpStart for firefox
Name:		firefox-ext-jumpstart
Version:	0.5a5.4.3
Release:	4
License:	MPL
Group:		Networking/WWW
URL:		https://addons.mozilla.org/en-US/firefox/addon/8914
Source:		http://releases.mozilla.org/pub/mozilla.org/addons/8914/%{srcname}-%{version}-fx.xpi
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	firefox >= %{firefox_version}
Obsoletes:	%{name} < %{version}-%{release}
BuildArch:	noarch
BuildRequires:	firefox-devel

%description
When you open a new tab get immediate access to your most frequently
used sites, bookmarks, closed tabs, history search.
Similar to Google's Chrome new tab feature.

%prep
%setup -q -c -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi

extdir="%{firefox_extdir}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}



%changelog
* Sat Mar 19 2011 Funda Wang <fwang@mandriva.org> 0.5a5.4.3-2mdv2011.0
+ Revision: 646525
- obsoletes old packages

* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 0.5a5.4.3-1
+ Revision: 633594
- new version 0.5a5.4.3

* Wed Jan 05 2011 Thierry Vignaud <tv@mandriva.org> 0.5a5.4.1-7mdv2011.0
+ Revision: 628873
- rebuild for new firefox

* Sun Nov 14 2010 Thierry Vignaud <tv@mandriva.org> 0.5a5.4.1-6mdv2011.0
+ Revision: 597401
- rebuild for new firefox

* Thu Oct 28 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5a5.4.1-5mdv2011.0
+ Revision: 589693
- update to 0.5a5.4.1

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 0.5a5.3-5mdv2011.0
+ Revision: 561161
- rebuild for ff 3.6.8

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 0.5a5.3-4mdv2010.1
+ Revision: 549359
- rebuild with FF 3.6.6

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 0.5a5.3-3mdv2010.1
+ Revision: 531095
- rebuild

* Wed Mar 24 2010 Funda Wang <fwang@mandriva.org> 0.5a5.3-2mdv2010.1
+ Revision: 527009
- rebuild

* Fri Mar 05 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5a5.3-1mdv2010.1
+ Revision: 514786
- import firefox-ext-jumpstart


* Fri Mar 05 2010 Pedro Fragoso <pedro.fragoso@caixamagica.pt> firefox-ext-jumpstart-0.5a5.3-1
- Initial release for Mandriva
