%define srcname new_tab_jumpstart

Summary:	New Tab JumpStart for firefox
Name:		firefox-ext-jumpstart
Version:	0.5a5.4.3
Release:	%mkrel 2
License:	MPL
Group:		Networking/WWW
URL:		https://addons.mozilla.org/en-US/firefox/addon/8914
Source:		http://releases.mozilla.org/pub/mozilla.org/addons/8914/%{srcname}-%{version}-fx.xpi
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	firefox >= %{firefox_epoch}:%{firefox_version}
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

