import Disclaimer from '../components/Disclaimer';

const featureCards = [
  {
    title: 'Why rapid screening matters',
    description: 'Fast preliminary screening can help identify when further evaluation may be appropriate after a head impact.',
  },
  {
    title: 'Eye movement analysis',
    description: 'Prototype gaze tracking and motion consistency provide an early educational signal for visual processing patterns.',
  },
  {
    title: 'Cognitive analysis',
    description: 'Reaction, memory, and attention tasks offer a quick snapshot of processing performance.',
  },
  {
    title: 'AI-powered feature analysis',
    description: 'Feature extraction combines signals into a structured prototype score for demonstration use.',
  },
];

export default function HomePage({ navigate }) {
  return (
    <div className="page">
      <header className="brand-bar">
        <div className="brand-mark"><span>SY</span> SYNORA AI</div>
        <div className="signal-status"><i /> PROTOTYPE SYSTEM / READY</div>
      </header>

      <section className="hero">
        <div className="hero-copy">
          <div className="eyebrow">FIELD LAB 01 <span /> RAPID SCREENING</div>
          <h1>SYNORA AI</h1>
          <p className="hero-kicker">A second look after impact.</p>
          <p className="subtitle">Rapid preliminary screening through eye movement and cognitive analysis.</p>

          <div className="hero-actions">
            <button className="primary-btn" onClick={() => navigate('/profile')}>
              START SCREENING
            </button>
            <button className="secondary-btn" onClick={() => document.getElementById('protocol')?.scrollIntoView()}>
              VIEW THE PROTOCOL
            </button>
          </div>

          <Disclaimer />
        </div>

        <div className="hero-panel">
          <div className="panel-topline">
            <span>NEURO-VISION / 04</span>
            <span>LIVE PREVIEW</span>
          </div>
          <div className="focus-visual">
            <div className="focus-grid" />
            <div className="focus-crosshair"><span /></div>
            <div className="focus-label focus-label-top">VISUAL TRACKING</div>
            <div className="focus-label focus-label-bottom">HEAD STILL / EYES ACTIVE</div>
          </div>
          <div className="hero-panel-copy">
            <p className="panel-index">01 / 04</p>
            <h2>Measure patterns.<br /><em>Guide the next step.</em></h2>
          </div>
          <div className="hero-stat-grid">
            <div className="stat-box">
              <small>Screening focus</small>
              <strong>Eye + cognition</strong>
            </div>
            <div className="stat-box">
              <small>Approach</small>
              <strong>Feature-based</strong>
            </div>
            <div className="stat-box">
              <small>Model status</small>
              <strong>Prototype</strong>
            </div>
            <div className="stat-box">
              <small>Safety</small>
              <strong>Educational</strong>
            </div>
          </div>
        </div>
      </section>

      <section className="section-block protocol-section" id="protocol">
        <div className="section-header">
          <div>
            <div className="eyebrow">THE PROTOCOL</div>
            <h2>Four signals. One clear snapshot.</h2>
          </div>
          <span className="protocol-time">~ 05 MINUTES</span>
        </div>
        <div className="protocol-rail">
          {['Profile + symptoms', 'Eye movement', 'Cognitive tasks', 'Screening summary'].map((item, index) => (
            <div className="protocol-step" key={item}>
              <span>{String(index + 1).padStart(2, '0')}</span>
              <strong>{item}</strong>
            </div>
          ))}
        </div>
        <div className="feature-grid">
          {featureCards.map((card) => (
            <article key={card.title} className="info-card">
              <h3>{card.title}</h3>
              <p>{card.description}</p>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}
