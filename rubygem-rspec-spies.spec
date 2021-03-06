#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rspec-spies
Version  : 2.1.4
Release  : 7
URL      : https://rubygems.org/downloads/rspec-spies-2.1.4.gem
Source0  : https://rubygems.org/downloads/rspec-spies-2.1.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-appraisal
BuildRequires : rubygem-bundler
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-jeweler
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
= rspec-spies
{<img src="https://travis-ci.org/technicalpickles/rspec-spies.png" />}[https://travis-ci.org/technicalpickles/rspec-spies]

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rspec-spies-2.1.4
gem spec %{SOURCE0} -l --ruby > rubygem-rspec-spies.gemspec

%build
gem build rubygem-rspec-spies.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rspec-spies-2.1.4.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/rspec-spies-2.1.4
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rspec-spies-2.1.4.gem
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/.document
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/Appraisals
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/Gemfile.lock
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/VERSION
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/gemfiles/rspec_2_11.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/gemfiles/rspec_2_11.gemfile.lock
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/gemfiles/rspec_2_12.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/gemfiles/rspec_2_12.gemfile.lock
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/gemfiles/rspec_2_13.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/gemfiles/rspec_2_13.gemfile.lock
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/lib/rspec-spies.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/rspec-spies.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/spec/rspec-spies_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/spec/spec.opts
/usr/lib64/ruby/gems/2.3.0/gems/rspec-spies-2.1.4/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/rspec-spies-2.1.4.gemspec
