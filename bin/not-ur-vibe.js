#!/usr/bin/env node

/**
 * Not Your Vibe CLI Runner
 * Supports: init, doctor, export, and install across Antigravity, Claude, Codex, and Cursor.
 */

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const args = process.argv.slice(2);
const command = args[0] || 'help';

const ROOT_DIR = path.resolve(__dirname, '..');

function printBanner() {
  console.log(`
  ╭─────────────────────────────────────────────────────────────╮
  │                    ✨ Not Your Vibe ✨                      │
  │     Universal Learning-First AI Pair Programming Framework  │
  │        You Architect. AI Mentors, Audits & Writes.          │
  ╰─────────────────────────────────────────────────────────────╯
  `);
}

function printHelp() {
  printBanner();
  console.log(`
  Usage:
    not-ur-vibe <command> [options]
    npx not-ur-vibe <command>

  Commands:
    init [path]         Initialize Not Your Vibe rules & skills in target folder
    doctor              Verify environment, configs, and agent health
    export [path]       Export your learning notes to a standalone portfolio
    help                Show this help message

  Supported AI Environments:
    • Google Antigravity (.agents/skills, AGENTS.md, GEMINI.md)
    • Claude Code (.claude-plugin, hooks, /learn, /reset)
    • OpenAI Codex (.codex-plugin, $learn, $reset)
    • Cursor IDE (.cursor/rules, .cursorrules)
    • Windsurf & GitHub Copilot (CLAUDE.md, .github/copilot-instructions.md)
  `);
}

function initProject(targetPath = '.') {
  printBanner();
  const targetDir = path.resolve(process.cwd(), targetPath);
  console.log(`🚀 Initializing Not Your Vibe in: ${targetDir}\n`);

  // Ensure directories exist
  const dirsToCreate = [
    '.vibewise',
    '.agents/skills/learn',
    '.agents/skills/reset',
    '.agents/skills/review',
    '.cursor/rules',
    '.github'
  ];

  dirsToCreate.forEach(d => {
    const fullPath = path.join(targetDir, d);
    if (!fs.existsSync(fullPath)) {
      fs.mkdirSync(fullPath, { recursive: true });
    }
  });

  // Copy or write AGENTS.md
  const agentsSrc = path.join(ROOT_DIR, 'AGENTS.md');
  const agentsDest = path.join(targetDir, 'AGENTS.md');
  if (fs.existsSync(agentsSrc) && !fs.existsSync(agentsDest)) {
    fs.copyFileSync(agentsSrc, agentsDest);
    console.log('  ✔ Created AGENTS.md (Universal master agent directives)');
  }

  // Copy or write .cursorrules
  const cursorSrc = path.join(ROOT_DIR, '.cursorrules');
  const cursorDest = path.join(targetDir, '.cursorrules');
  if (fs.existsSync(cursorSrc) && !fs.existsSync(cursorDest)) {
    fs.copyFileSync(cursorSrc, cursorDest);
    console.log('  ✔ Created .cursorrules (Cursor IDE integration)');
  }

  // Create initial .vibewise state templates
  const profileDest = path.join(targetDir, '.vibewise', 'profile.md');
  if (!fs.existsSync(profileDest)) {
    fs.writeFileSync(profileDest, `# Learner Profile\n\nLearning mode: active\nOnboarding: incomplete\n\nRemaining onboarding: Project situation, experience, stack familiarity, goals, and preferences.\n`, 'utf-8');
    console.log('  ✔ Created .vibewise/profile.md');
  }

  const progressDest = path.join(targetDir, '.vibewise', 'progress.md');
  if (!fs.existsSync(progressDest)) {
    fs.writeFileSync(progressDest, `# Learning Progress\n\nNo learning events recorded yet.\n`, 'utf-8');
    console.log('  ✔ Created .vibewise/progress.md');
  }

  const mapDest = path.join(targetDir, '.vibewise', 'project-map.md');
  if (!fs.existsSync(mapDest)) {
    fs.writeFileSync(mapDest, `# Project Map\n\nNot mapped yet. Inspect current project files.\n`, 'utf-8');
    console.log('  ✔ Created .vibewise/project-map.md');
  }

  // Suggest gitignore update
  const gitignorePath = path.join(targetDir, '.gitignore');
  if (fs.existsSync(gitignorePath)) {
    const gitignoreContent = fs.readFileSync(gitignorePath, 'utf-8');
    if (!gitignoreContent.includes('.vibewise/')) {
      fs.appendFileSync(gitignorePath, '\n# Not Your Vibe learning state\n.vibewise/\n');
      console.log('  ✔ Added .vibewise/ to .gitignore');
    }
  } else {
    fs.writeFileSync(gitignorePath, '# Not Your Vibe learning state\n.vibewise/\n', 'utf-8');
    console.log('  ✔ Created .gitignore with .vibewise/');
  }

  console.log(`
  ✅ Successfully initialized Not Your Vibe!
  
  Next Steps:
  1. Open this project in your AI editor (Antigravity, Claude Code, Codex, or Cursor).
  2. In chat, type "/learn" (or "$learn" in Codex) or ask: "Let's build something together!"
  3. Enjoy learning while you architect and your AI writes!
  `);
}

function runDoctor() {
  printBanner();
  const scriptPath = path.join(ROOT_DIR, 'scripts', 'doctor.py');
  if (fs.existsSync(scriptPath)) {
    const pyCmd = process.platform === 'win32' ? 'python' : 'python3';
    const res = spawnSync(pyCmd, [scriptPath, '--cwd', process.cwd()], { stdio: 'inherit' });
    if (res.error) {
      console.log('  ℹ Python is required for automated doctor diagnostics.');
    }
  } else {
    console.log('  Diagnostic script not found at', scriptPath);
  }
}

function runExport(targetPath = '.') {
  const scriptPath = path.join(ROOT_DIR, 'scripts', 'export_notes.py');
  const pyCmd = process.platform === 'win32' ? 'python' : 'python3';
  spawnSync(pyCmd, [scriptPath, '--cwd', path.resolve(process.cwd(), targetPath)], { stdio: 'inherit' });
}

switch (command) {
  case 'init':
    initProject(args[1]);
    break;
  case 'doctor':
    runDoctor();
    break;
  case 'export':
    runExport(args[1]);
    break;
  case 'help':
  default:
    printHelp();
    break;
}
