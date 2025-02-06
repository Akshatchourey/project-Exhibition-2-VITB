// home elements
document.addEventListener("DOMContentLoaded",()=>{
    // Counter Animation
    const counters = document.querySelectorAll(".counter")
    const speed = 200
  
    const animateCounter = (counter) => {
      const target = +counter.getAttribute("data-target")
      let count = 0
      const increment = target / speed
  
      const updateCount = () => {
        count += increment
        if (count < target) {
          counter.innerText = Math.ceil(count)
          requestAnimationFrame(updateCount)
        } else {
          counter.innerText = target
        }
      }
      updateCount()
    }
  
    // Scroll Reveal Animation
    const scrollReveal = () => {
      const elements = document.querySelectorAll(".scroll-reveal")
      elements.forEach((element) => {
        const elementTop = element.getBoundingClientRect().top
        const elementVisible = 150
  
        if (elementTop < window.innerHeight - elementVisible) {
          element.classList.add("active")
        }
      })
    }
  
    // Initialize counter animation when elements are in view
    const observeCounters = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCounter(entry.target)
          observeCounters.unobserve(entry.target)
        }
      })
    })
  
    counters.forEach((counter) => observeCounters.observe(counter))
  
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        e.preventDefault()
        const target = document.querySelector(this.getAttribute("href"))
        if (target) {
          target.scrollIntoView({
            behavior: "smooth",
          })
        }
      })
    })
  
    // Parallax effect for hero section
    const hero = document.querySelector(".hero")
    window.addEventListener("scroll", () => {
      const scrolled = window.pageYOffset
      hero.style.backgroundPositionY = scrolled * 0.5 + "px"
    })
  
    // Initialize scroll reveal animation
    window.addEventListener("scroll", scrollReveal)
    scrollReveal()
  
    // Navbar scroll effect
    const nav = document.querySelector("nav")
    let lastScroll = 0
  
    window.addEventListener("scroll", () => {
      const currentScroll = window.pageYOffset
  
      if (currentScroll <= 0) {
        nav.classList.remove("scroll-up")
        return
      }
  
      if (currentScroll > lastScroll && !nav.classList.contains("scroll-down")) {
        nav.classList.remove("scroll-up")
        nav.classList.add("scroll-down")
      } else if (currentScroll < lastScroll && nav.classList.contains("scroll-down")) {
        nav.classList.remove("scroll-down")
        nav.classList.add("scroll-up")
      }
      lastScroll = currentScroll
    })
  
    // Value cards hover effect
    const valueCards = document.querySelectorAll(".value-card")
    valueCards.forEach((card) => {
      card.addEventListener("mouseenter", () => {
        card.style.transform = "translateY(-10px)"
      })
      card.addEventListener("mouseleave", () => {
        card.style.transform = "translateY(0)"
      })
    })
  
    // Team member image hover effect
    const teamMembers = document.querySelectorAll(".team-member")
    teamMembers.forEach((member) => {
      const image = member.querySelector("img")
      member.addEventListener("mouseenter", () => {
        image.style.transform = "scale(1.1)"
      })
      member.addEventListener("mouseleave", () => {
        image.style.transform = "scale(1)"
      })
    })
  })
  
  