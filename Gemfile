source "https://rubygems.org"

gem "jekyll", "~> 4.3.0"
gem "jekyll-seo-tag"
gem "jekyll-sitemap"

# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :install_if => Gem.win_platform?

# Lock `http_parser_rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser_rb", "~> 0.6.0", :platforms => [:jruby]

# Use `debug` to add debug prints
gem "debug", platforms: %i[mri mingw x64_mingw]
