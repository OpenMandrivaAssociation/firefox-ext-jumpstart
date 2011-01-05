%define _mozillaextpath %{firefox_mozillapath}/extensions

%define srcname new_tab_jumpstart

Summary:	New Tab JumpStart for firefox
Name:		firefox-ext-jumpstart
Version:	0.5a5.4.1
Release:	%mkrel 7
License:	MPL
Group:		Networking/WWW
URL:		https://addons.mozilla.org/en-US/firefox/addon/8914
Source:		http://releases.mozilla.org/pub/mozilla.org/addons/8914/%{srcname}-%{version}-fx.xpi
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	mozilla-firefox => %{firefox_epoch}:%{firefox_version}
BuildRequires:	firefox-devel

%description
When you open a new tab get immediate access to your most frequently
used sites, bookmarks, closed tabs, history search.
Similar to Google's Chrome new tab feature.

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi

extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %firefox_mozillapath
%{_mozillaextpath}

