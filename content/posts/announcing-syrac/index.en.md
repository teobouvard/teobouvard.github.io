---
date: 2025-07-11T18:30:00+02:00
title: Announcing Syrac
summary: A paragliding time attack platform.
tags:
  - syrac
  - paragliding
  - software
cover: interlaken_t3.png
---

# TL;DR

Head to [app.syrac.org](https://app.syrac.org), complete tasks you like, and see how high you can climb on the leaderboards.

# Permanent tasks are great

I've always loved the idea of permanent paragliding tasks.
You complete them just like during regular paragliding competitions, except you can retry them as many times as you want.
This allows you to use the same set of turnpoints under completely different conditions, making each attempt unique.

Different lines, different thermals, different times. Each flight becomes a puzzle to solve.

Some hardcore XC pilots might think this is stupid, that you should always strive to get the most out of every day by exploring new routes and chasing big distances.
But I believe permanent tasks offer something equally valuable: the ability to truly master a route, to understand how conditions affect your strategy, and to push your limits, even on average-looking days.

If you want to know more about the philosophy behind permanent tasks, read the [manifesto](https://docs.syrac.org/manifesto).

# The problem

Until now, permanent tasks were kind of a niche concept.
Some well-known flying sites run their local tasks, but they're hard to discover unless you're a local pilot or know exactly where to look.

There's no place to find interesting tasks or compare your times with pilots worldwide.

# Introducing Syrac

That's why I've been building [Syrac](https://app.syrac.org), a platform where you can:

* **Discover tasks** from flying sites around the world
* **Compete** on leaderboards with other pilots
* **Share your own tasks** and build a community around your local site

The [rules](https://docs.syrac.org/rules) explain in more detail how to participate.

{{< image src="explore_map.png" alt="Syrac explore map screenshot" position="center" style="border-radius: 4px;" >}}

# What's next

There are still rough edges—the most obvious being that we're in 2025 and there's still no easy way to actually build a task from scratch!

For now, the least annoying workflow might be to:

* Design the route in [flyXC](https://flyxc.app/)
* Export it in XCTrack format
* Set the task type and turnpoint radii in [XCTrack](https://xctrack.org/)
* Export it and upload to Syrac

You can also use [TaskCreator](https://www.vololiberomontecucco.it/taskcreator/), but you'll need a waypoint file to get started.

A built-in task builder with a nice UI is on the roadmap, but I wanted to get Syrac out in the open now that the core features are ready.

# Get involved

Whether you're looking to challenge yourself on existing tasks or share your favorite local routes with the global community, Syrac is built for you.

Try it out at [app.syrac.org](https://app.syrac.org) and [submit feedback on GitHub](https://github.com/orgs/syrac-org/discussions/new/choose) if you've got suggestions or ideas.
