# Generated from rest-client-2.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rest-client

# This will enable test on the future
# and also added it depdendencies
%global with_test 0

Name: rubygem-%{gem_name}
Version: 2.0.2
Release: 1%{?dist}
Summary: HTTP & REST client for ruby
Group: Development/Languages
License: MIT
URL: https://github.com/rest-client/rest-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0.0
%if 0%{?with_test}
BuildRequires: rubygem(webmock) >= 2.0
BuildRequires: rubygem(webmock) < 3
BuildRequires: rubygem(rspec) >= 3.0
BuildRequires: rubygem(rspec) < 4
BuildRequires: rubygem(pry)
BuildRequires: rubygem(pry) < 1
BuildRequires: rubygem(pry-doc)
BuildRequires: rubygem(pry-doc) < 1
BuildRequires: rubygem(rubocop)
BuildRequires: rubygem(rubocop) < 1
%endif
BuildArch: noarch

Provides: rubygem(%{gem_name}) = %{version}

%description
A simple HTTP and REST client for Ruby, inspired by the Sinatra microframework
style of specifying actions: get, put, post, delete.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{_bindir}/restclient
%exclude %{gem_instdir}/.gitignore
%{gem_instdir}/.rubocop-disables.yml
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_instdir}/rest-client.gemspec
%exclude %{gem_instdir}/rest-client.windows.gemspec
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/history.md
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/AUTHORS
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/history.md
%{gem_instdir}/spec

%changelog
* Tue Jun 20 2017 Juan Badia Payno <jbadiapa@redhat.com> - 2.0.2-1
- Created Package CentOS

* Tue Feb 07 2017 Vít Ondruch <vondruch@redhat.com> - 2.0.0-2
- Fix compatibility with Ruby OpenSSL 2.x+.

* Thu Jul 14 2016 Jun Aruga <jaruga@redhat.com> - 2.0.0-1
- Update to rest-client 2.0.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 19 2015 Vít Ondruch <vondruch@redhat.com> - 1.8.0-1
- Update to rest-client 1.8.0.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 1.6.7-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Sat Sep 22 2012 Tim Bielawa <tim@redhat.com> - 1.6.7-1
- Update to 1.6.7

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Vít Ondruch <vondruch@redhat.com> - 1.6.1-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 08 2010 Michal Fojtik <mfojtik@redhat.com> - 1.6.1-1
- New version release

* Wed Mar 03 2010 Michal Fojtik <mfojtik@redhat.com> - 1.4.0-6
- New version release

* Wed Feb 17 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-5
- Added %%dir %%{geminstdir} into spec file

* Wed Feb 17 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-4
- Marked README.rdoc, history.md and spec/ as %%doc

* Tue Feb 16 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-3
- Fixed licence (MIT)
- Fixed duplicated files in spec
- Replaced %%define with %%global

* Tue Feb 16 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-2
- Fixed spec filename
- Added Ruby dependency

* Tue Feb 16 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-1
- Initial package
